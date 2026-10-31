// ============================================================================
// [Lab 08] 3D Vectors, Euler Angles & WorldToScreen (Tier B- | Diff: 5.0/10)
// ============================================================================
// PURPOSE:
//   Builds on Lab 07. Moving from 2D stats into 3D FPS/Action engines
//   (Aim Hero, AssaultCube, CS 1.6, KovaaK's) requires understanding 3D
//   Vector Algebra: Euclidean Distance, Pitch/Yaw Euler Angles, and 4x4
//   View-Projection Matrix WorldToScreen (W2S) math!
//
// QUEST OBJECTIVE:
//   3 Phantom Drones hover in 3D space around your camera at (0, 0, 0).
//   To lock onto each drone, compute (or write in Cheat Engine / external C++)
//   the exact Camera Yaw & Pitch angles pointing to the active drone!
// ============================================================================

#include <iostream>
#include <cmath>
#include <cstdint>
#include <iomanip>

constexpr float PI = 3.14159265358979323846f;

struct Vec3 {
    float x, y, z;
};

struct CameraState {
    Vec3  position;           // +0x00 (x, y, z)
    float pitchDegrees;       // +0x0C (-89 to +89)
    float yawDegrees;         // +0x10 (-180 to +180)
    float fovDegrees;         // +0x14
    float viewProjMatrix[16]; // +0x18 (4x4 Matrix)
};

struct PhantomDrone {
    int32_t id;       // +0x00
    int32_t active;   // +0x04
    Vec3    worldPos; // +0x08 (x, y, z)
};

CameraState g_Camera = {
    { 0.0f, 0.0f, 0.0f },
    0.0f, 0.0f, 90.0f,
    {
        1.0f, 0.0f, 0.0f, 0.0f,
        0.0f, 1.0f, 0.0f, 0.0f,
        0.0f, 0.0f, 1.0f, 0.0f,
        0.0f, 0.0f, 0.0f, 1.0f
    }
};

PhantomDrone g_Drones[3] = {
    { 1, 1, { 100.0f,  100.0f,   0.0f } }, // Yaw = 45.0,  Pitch = 0.0
    { 2, 1, {   0.0f, -200.0f, 200.0f } }, // Yaw = -90.0, Pitch = 45.0
    { 3, 1, { -50.0f,   86.6025f, -50.0f } } // Yaw = 120.0, Pitch = -26.565
};

void ComputeRequiredAngles(const Vec3& cam, const Vec3& target, float& outPitch, float& outYaw) {
    float dx = target.x - cam.x;
    float dy = target.y - cam.y;
    float dz = target.z - cam.z;
    float dist2D = std::sqrt(dx * dx + dy * dy);
    outYaw   = std::atan2(dy, dx) * (180.0f / PI);
    outPitch = std::atan2(dz, dist2D) * (180.0f / PI);
}

int main() {
    std::cout << "Select Training Mode:\n  [1] Apprentice Mode (Shows Struct Addresses & Math Formulas)\n  [2] Hardcore Mode (Blind)\n> ";
    int mode = 1;
    if (!(std::cin >> mode)) return 0;
    bool blind = (mode == 2);

    int currentDrone = 0;
    while (currentDrone < 3) {
        PhantomDrone& d = g_Drones[currentDrone];
        float reqPitch = 0.0f, reqYaw = 0.0f;
        ComputeRequiredAngles(g_Camera.position, d.worldPos, reqPitch, reqYaw);

        std::cout << "\n====================================================================\n";
        std::cout << "  [LAB 08 | TIER B-] 3D AIM & WORLD-TO-SCREEN SIMULATOR\n";
        std::cout << "====================================================================\n";
        std::cout << std::fixed << std::setprecision(2);
        std::cout << "  Camera Position : (" << g_Camera.position.x << ", " << g_Camera.position.y << ", " << g_Camera.position.z << ")\n";
        std::cout << "  Camera Angles   : Pitch = " << g_Camera.pitchDegrees << " deg | Yaw = " << g_Camera.yawDegrees << " deg\n";
        std::cout << "  Active Drone #" << d.id << " : World Pos = (" << d.worldPos.x << ", " << d.worldPos.y << ", " << d.worldPos.z << ")\n";

        if (!blind) {
            std::cout << "--------------------------------------------------------------------\n";
            std::cout << "  &g_Camera.pitchDegrees : 0x" << std::hex << (uintptr_t)&g_Camera.pitchDegrees << "\n";
            std::cout << "  &g_Camera.yawDegrees   : 0x" << (uintptr_t)&g_Camera.yawDegrees << "\n";
            std::cout << "  &g_Drones[0]           : 0x" << (uintptr_t)&g_Drones[0] << std::dec << "\n";
            std::cout << "  [Math Hint] Yaw = atan2(dy, dx) * 180/PI | Pitch = atan2(dz, sqrt(dx^2+dy^2)) * 180/PI\n";
        }
        std::cout << "====================================================================\n";
        std::cout << "Actions:\n";
        std::cout << "  [1] Fire Railgun at Current Camera Pitch/Yaw\n";
        std::cout << "  [2] Manually Enter Pitch & Yaw Angles\n";
        std::cout << "  [0] Exit Lab\n> ";

        int choice = 0;
        if (!(std::cin >> choice) || choice == 0) break;

        if (choice == 2) {
            std::cout << "Enter Pitch (deg): "; std::cin >> g_Camera.pitchDegrees;
            std::cout << "Enter Yaw   (deg): "; std::cin >> g_Camera.yawDegrees;
        }

        float errPitch = std::fabs(g_Camera.pitchDegrees - reqPitch);
        float errYaw   = std::fabs(g_Camera.yawDegrees - reqYaw);

        if (errPitch < 0.5f && errYaw < 0.5f) {
            d.active = 0;
            currentDrone++;
            std::cout << "\n>> [DIRECT HIT!] Phantom Drone #" << d.id << " vaporized!\n";
        } else {
            std::cout << "\n>> [MISSED!] Angular error too large (Delta Pitch: " << errPitch
                      << " deg, Delta Yaw: " << errYaw << " deg).\n";
            std::cout << "   Calculate the exact Euler angles from g_Camera to g_Drones[" << currentDrone << "]!\n";
        }
    }

    if (currentDrone >= 3) {
        std::cout << "\n********************************************************************\n";
        std::cout << "  [QUEST COMPLETE - TIER B- CLEARED!]\n";
        std::cout << "  You mastered 3D Euclidean Vectors and Pitch/Yaw Euler Angles!\n";
        std::cout << "  Next Step: Proceed to Lab 09 (Internal DLL Injection & Hooking).\n";
        std::cout << "********************************************************************\n";
    }
    return 0;
}
