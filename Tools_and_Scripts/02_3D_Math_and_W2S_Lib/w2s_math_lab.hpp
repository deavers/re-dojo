// ============================================================================
// [Tool 02] 3D Math, Euler Angles & WorldToScreen Header Library
// ============================================================================
// PURPOSE:
//   Drop-in C++20 header for Stage 6 (3D Math & ESP Overlays):
//     - Vec3 & Vec2 vector operations (Dot product, Cross product, Distance)
//     - CalcEulerAngles() for 3D camera aim calculation (Lab 08, Aim Hero, CS 1.6)
//     - WorldToScreen_RowMajor() (DirectX / Unreal Engine)
//     - WorldToScreen_ColMajor() (OpenGL / Unity / AssaultCube)
// ============================================================================

#pragma once
#include <cmath>

namespace REMath {

constexpr float kPi = 3.14159265358979323846f;

struct Vec2 {
    float x = 0.0f;
    float y = 0.0f;
};

struct Vec3 {
    float x = 0.0f;
    float y = 0.0f;
    float z = 0.0f;

    Vec3 operator+(const Vec3& rhs) const { return { x + rhs.x, y + rhs.y, z + rhs.z }; }
    Vec3 operator-(const Vec3& rhs) const { return { x - rhs.x, y - rhs.y, z - rhs.z }; }
    Vec3 operator*(float s)         const { return { x * s, y * s, z * s }; }

    float Length() const { return std::sqrt(x * x + y * y + z * z); }
    float Length2D() const { return std::sqrt(x * x + y * y); }
    float DistanceTo(const Vec3& other) const { return (*this - other).Length(); }
    float Dot(const Vec3& rhs) const { return x * rhs.x + y * rhs.y + z * rhs.z; }
};

// Computes Camera Pitch & Yaw (in degrees) from `cameraPos` to `targetPos`
inline void CalcEulerAngles(const Vec3& cameraPos, const Vec3& targetPos, float& outPitchDeg, float& outYawDeg) {
    Vec3 delta = targetPos - cameraPos;
    float hyp2D = delta.Length2D();
    outYawDeg   = std::atan2(delta.y, delta.x) * (180.0f / kPi);
    outPitchDeg = std::atan2(delta.z, hyp2D)   * (180.0f / kPi);
}

// DirectX Row-Major 4x4 ViewProjection Matrix WorldToScreen
inline bool WorldToScreen_RowMajor(
    const Vec3& worldPos,
    const float m[16],
    float screenWidth,
    float screenHeight,
    Vec2& outScreen)
{
    float clipX = worldPos.x * m[0]  + worldPos.y * m[1]  + worldPos.z * m[2]  + m[3];
    float clipY = worldPos.x * m[4]  + worldPos.y * m[5]  + worldPos.z * m[6]  + m[7];
    float clipW = worldPos.x * m[12] + worldPos.y * m[13] + worldPos.z * m[14] + m[15];

    if (clipW < 0.01f) return false; // Target is behind the camera

    float ndcX = clipX / clipW;
    float ndcY = clipY / clipW;

    outScreen.x = (screenWidth  * 0.5f) * (1.0f + ndcX);
    outScreen.y = (screenHeight * 0.5f) * (1.0f - ndcY);
    return true;
}

// OpenGL / AssaultCube / Unity Column-Major 4x4 ViewProjection Matrix WorldToScreen
inline bool WorldToScreen_ColMajor(
    const Vec3& worldPos,
    const float m[16],
    float screenWidth,
    float screenHeight,
    Vec2& outScreen)
{
    float clipX = worldPos.x * m[0] + worldPos.y * m[4] + worldPos.z * m[8]  + m[12];
    float clipY = worldPos.x * m[1] + worldPos.y * m[5] + worldPos.z * m[9]  + m[13];
    float clipW = worldPos.x * m[3] + worldPos.y * m[7] + worldPos.z * m[11] + m[15];

    if (clipW < 0.01f) return false;

    float ndcX = clipX / clipW;
    float ndcY = clipY / clipW;

    outScreen.x = (screenWidth  * 0.5f) * (1.0f + ndcX);
    outScreen.y = (screenHeight * 0.5f) * (1.0f - ndcY);
    return true;
}

} // namespace REMath
