#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

static float Q_rsqrt(float number) {
    long i;
    float x2, y;
    const float threehalfs = 1.5F;

    x2 = number * 0.5F;
    y = number;
    i = *(long*)&y;             // evil floating point bit level hacking
    i = 0x5f3759df - (i >> 1);  // what the [...]?
    y = *(float*)&i;
    y = y * (threehalfs - (x2 * y * y));  // 1st iteration
    //    y = y * (threehalfs - (x2 * y * y));  // 2nd iteration, this can be removed

    return y;
}

static double err(double d, float f) {
    double denominator = fabs(d);
    if (denominator == 0.0) {
        return 0.0;
    }
    return fabs(f - d) / denominator;
}

int main(void) {
    const int N = 1000;
    const float X_MAX = 1.0e6f;
    const float EPSILON = 1e-6f;

    srand((unsigned int)time(NULL));

    printf("x,err_quake,err_sqrtf\n");

    for (int n = 0; n < N; n++) {
        float r = (float)rand() / (float)RAND_MAX;
        float x = r * X_MAX + EPSILON;

        double d = 1.0 / sqrt((double)x);

        float quake = Q_rsqrt(x);
        double quake_err = err(d, quake);

        float csqrtf = 1.0f / sqrtf(x);
        double sqrtf_err = err(d, csqrtf);

        printf("%.9g,%.17g,%.17g\n", (double)x, quake_err, sqrtf_err);
    }

    return 0;
}
