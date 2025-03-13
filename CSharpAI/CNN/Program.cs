using OpenCvSharp;

string imagePath = Path.Combine(AppContext.BaseDirectory, "..", "..", "..", "Resource", "2.png");
var image = Cv2.ImRead(imagePath, ImreadModes.Color);

Cv2.ImShow("Origin Image", image);

var kernel = new float[,]
{
    { -1f, 0, 1f},
    { -1f, 0, 1f},
    { -1f, 0, 1f},
};

Mat filter = new Mat(3, 3, MatType.CV_32F);
for (int i = 0; i < 3; i++)
    for (int j = 0; j < 3; j++)
        filter.Set<float>(i, j, kernel[i,j]);

Mat result = new Mat();
Cv2.Filter2D(image, result, MatType.CV_8UC3, filter);
var resultImage = Filter(image, filter);
////resultImage.ConvertTo(resultImage, MatType.CV_8UC3);
//resultImage = Convert32FC3To8UC3(resultImage);

var myResult = new Mat(image.Size(), MatType.CV_32FC3, new Scalar(0));
#region do Convolution
for (int y = 1; y < image.Rows - 1; y++) // 경계 피하기
{
    for (int x = 1; x < image.Cols - 1; x++)
    {
        var sum = new float[3] { 0, 0, 0 };

        for (int ky = -1; ky <= 1; ky++)
        {
            for (int kx = -1; kx <= 1; kx++)
            {
                var pixelValue = image.At<Vec3b>(y + ky, x + kx);
                sum[0] += pixelValue[0] * kernel[ky + 1, kx + 1];
                sum[1] += pixelValue[1] * kernel[ky + 1, kx + 1];
                sum[2] += pixelValue[2] * kernel[ky + 1, kx + 1];
            }
        }

        myResult.Set<Vec3f>(y, x, new Vec3f(sum[0], sum[1], sum[2]));
    }
}
myResult.ConvertTo(myResult, MatType.CV_8UC3);
#endregion

Cv2.ImShow("Filtered Image", result);
Cv2.ImShow("Result Image", resultImage);
Cv2.ImShow("My Result", myResult);

Cv2.WaitKey();

Mat Filter(Mat img, Mat mask)
{
    var dst = new Mat(img.Rows, img.Cols, MatType.CV_8UC3, new Scalar(0));
    Point h_m = new Point(mask.Width / 2, mask.Height / 2); 

    for (int i = h_m.Y; i < img.Rows - h_m.Y; i++)
    {
        for (int j = h_m.X; j < img.Cols - h_m.X; j++)
        {
            var sum = new float[3] { 0, 0, 0 };

            for (int u = 0; u < mask.Rows; u++)
            {
                for (int v = 0; v < mask.Cols; v++)
                {
                    int y = i + u - h_m.Y;
                    int x = j + v - h_m.X;
                    var pixelValue = image.At<Vec3b>(y, x);
                    sum[0] += mask.At<float>(u, v) * pixelValue[0];
                    sum[1] += mask.At<float>(u, v) * pixelValue[1];
                    sum[2] += mask.At<float>(u, v) * pixelValue[2];
                }
            }
            dst.At<Vec3b>(i, j) = new Vec3b(ClampByte(sum[0], 0, 255),
                                            ClampByte(sum[1], 0, 255),
                                            ClampByte(sum[2], 0, 255));
        }
    }
    return dst;
}

// CV_32FC3에서 CV_8UC3로 변환하는 함수 (0 이하인 경우 0으로, 최대값에 맞춰 변환)
static Mat Convert32FC3To8UC3(Mat inputImage)
{
    // 결과 이미지를 위한 Mat 초기화 (CV_8UC3)
    Mat resultImage = new Mat(inputImage.Size(), MatType.CV_8UC3);

    // 값 변환
    for (int y = 0; y < inputImage.Rows; y++)
    {
        for (int x = 0; x < inputImage.Cols; x++)
        {
            Vec3f pixel = inputImage.At<Vec3f>(y, x);
            byte[] outputPixel = new byte[3];

            for (int c = 0; c < 3; c++) // RGB 채널에 대해 반복
            {
                // 0 이하인 경우 0으로 설정하고, 나머지는 그대로 변환
                outputPixel[c] = (byte)Clamp(pixel[c] < 0 ? 0 : pixel[c], 0, 255);
            }

            // 결과 이미지에 픽셀 값 설정
            resultImage.Set<Vec3b>(y, x, new Vec3b(outputPixel[0], outputPixel[1], outputPixel[2]));
        }
    }

    return resultImage;
}

// 클램프 함수 정의
static int Clamp(float value, int min, int max)
{
    if (value < min) return min;
    if (value > max) return max;
    return (int)value;
}

byte ClampByte(float value, byte min, byte max)
{
    if (value < min) return min;
    if (value > max) return max;
    return (byte)value;
}