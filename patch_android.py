"""Ajusta o projeto Android gerado pelo Capacitor: paisagem, tela cheia, sem hibernar a tela."""
import re, pathlib
base = pathlib.Path("android/app/src/main")

m = base / "AndroidManifest.xml"
t = m.read_text()
if "screenOrientation" not in t:
    t = t.replace("<activity", '<activity\n            android:screenOrientation="sensorLandscape"', 1)
m.write_text(t)

s = base / "res/values/styles.xml"
t = s.read_text()
extra = ('\n        <item name="android:windowFullscreen">true</item>'
         '\n        <item name="android:windowLayoutInDisplayCutoutMode">shortEdges</item>'
         '\n        <item name="android:keepScreenOn">true</item>')
if "windowFullscreen" not in t:
    t = re.sub(r'(<style name="AppTheme\.NoActionBar"[^>]*>)', r'\1' + extra, t, count=1)
s.write_text(t)

# modo imersivo (esconde barra de navegação)
for p in base.rglob("MainActivity.java"):
    t = p.read_text()
    if "SYSTEM_UI_FLAG_IMMERSIVE_STICKY" not in t:
        t = t.replace("public class MainActivity extends BridgeActivity {}", '''public class MainActivity extends BridgeActivity {
    @Override
    public void onWindowFocusChanged(boolean hasFocus) {
        super.onWindowFocusChanged(hasFocus);
        if (hasFocus) {
            getWindow().getDecorView().setSystemUiVisibility(
                android.view.View.SYSTEM_UI_FLAG_LAYOUT_STABLE
                | android.view.View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
                | android.view.View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN
                | android.view.View.SYSTEM_UI_FLAG_HIDE_NAVIGATION
                | android.view.View.SYSTEM_UI_FLAG_FULLSCREEN
                | android.view.View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY);
        }
    }
}''')
        p.write_text(t)
print("Projeto Android ajustado.")
