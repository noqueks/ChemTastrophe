# ChemTastrophe World — projeto APK (Capacitor)

O jogo fica em `www/` (o HTML virou `index.html`; assets intactos, exceto 2 arquivos de referência não usados pelo jogo).
O app abre em paisagem, tela cheia, e o progresso (localStorage) é salvo no aparelho.

## Opção A — sem instalar nada (GitHub Actions)
1. Crie um repositório no GitHub e envie o conteúdo desta pasta (inclusive `.github/`).
2. Aba **Actions → Build APK** (roda sozinho a cada push, ou clique em *Run workflow*).
3. Ao terminar (~5 min), baixe o artefato **ChemTastrophe-World-apk** → `app-debug.apk`.
4. Copie para o celular e instale (permita "fontes desconhecidas").

## Opção B — no seu computador
Com Node, JDK 17+ e Android SDK instalados: `./build_local.sh`
O APK sai em `android/app/build/outputs/apk/debug/app-debug.apk`.

## Atualizar o jogo
Substitua `www/index.html` / `www/assets` e gere o APK de novo.

## Observações
- É um APK *debug* (assinado com chave de debug): ótimo para instalar e testar. Para publicar na Play Store é preciso um build *release* assinado (AAB).
- O ícone padrão é o do Capacitor; para trocar, coloque seus PNGs em `android/app/src/main/res/mipmap-*` depois do `cap add`.
