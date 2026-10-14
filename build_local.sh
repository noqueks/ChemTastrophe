#!/usr/bin/env bash
# Requer: Node 18+, JDK 17+ e Android SDK (ANDROID_HOME configurado).
set -e
npm install
npx cap add android
python3 patch_android.py
npx cap sync android
(cd android && chmod +x gradlew && ./gradlew assembleDebug)
echo "APK: android/app/build/outputs/apk/debug/app-debug.apk"
