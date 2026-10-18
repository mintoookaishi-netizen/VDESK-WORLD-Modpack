# VDESK WORLD — Streamer MOD Test v1.0.0

> [!WARNING]
> **重要：このVDESK独自MODパックは、Modrinth内で公開・審査されていません。**
>
> Modrinth Appでこの外部ファイルを読み込むと **Unknown file warning（不明なファイルの警告）** が表示されます。これはVDESK独自パックがModrinth内で公開・審査されていないためで、**ウイルスを検出したという意味ではありません**。しかし、**安全性が保証されたという意味でもありません**。内容を確認し、納得できる場合にのみインストールしてください。警告を無効化する必要はありません。

配信者・参加者向けのMinecraft MOD互換性テスト用の配布リポジトリです。本番イベントのゲームデータやサーバー設定は含みません。

## ダウンロード・バージョン

**[VDESK_WORLD_MOD_TEST_v1.0.0.mrpack](VDESK_WORLD_MOD_TEST_v1.0.0.mrpack)**

- Minecraft Java: **1.21.11**
- Fabric Loader: **0.19.5**
- クライアントMOD: **29個（バージョン固定）**
- JAR取得元: 各MODについて **cdn.modrinth.com** の公式配布URLを参照
- .mrpack の SHA-256: **`f55cc57e02a45fc7196648a4652111f5e9f40f0abb786139fb1abae69ccfe14a`**

※ Modrinth公式CDNから取得する構成でも、Modrinthがこの独自パックを審査・承認したことにはなりません。

## インストール

1. [Modrinth App公式サイト](https://modrinth.com/app) からアプリを導入する。
2. このリポジトリから `VDESK_WORLD_MOD_TEST_v1.0.0.mrpack` をダウンロードする。
3. Modrinth Appの **Create an Instance → Import Instance（Import from file）** などから読み込む。UIの表示はアプリ版によって異なる。
4. **Unknown file warning** が出たら、これはModrinth内で公開・審査されていないパックであると理解し、[内容一覧](MODS.md) と [安全性について](SECURITY.md) を確認する。判断できない場合は **Don't install** を選ぶ。
5. 独立した専用Minecraftプロファイルを起動する。既存の `mods` フォルダへ直接上書きしない。
6. 運営から個別に案内される**テストサーバーの接続先**へ接続する。アカウントの許可登録が必要です。

## 1人での動作確認

| 検証内容 | ゲーム内で行うこと |
|---|---|
| 魔法・剣 | `/trigger vdesk_modkit set 1` |
| NPC生成・会話UI | `/trigger vdesk_npctest set 1` |
| カメラ | `/trigger vdesk_camtest set 1` |
| カメラ強制解除 | `/trigger vdesk_camskip set 1` |
| Simple Voice Chat | `V` キー → 設定 → マイク入力テスト |

マイクの入力テストは1人で可能ですが、相手に声が届くかどうかは2人以上で確認してください。テストワールドは本番ストーリーの再現ではありません。

**現時点の確認範囲:** テストサーバーの起動およびVC用ポートの起動は確認済みです。全29MODのクライアント実機テスト、外部公開経由の接続、実通話の成功はまだ保証できません。

## 中身をすべて確認する

- [MODS.md](MODS.md) — 29個のMOD名・公式ページ・バージョン固定ファイル
- [manifest.json](manifest.json) — 29件の取得URL、SHA-1、SHA-512、プロジェクト情報
- [modrinth.index.json](modrinth.index.json) — 配布`.mrpack`から抽出した元のインデックス
- [SHA256SUMS.txt](SHA256SUMS.txt) — 配布`.mrpack`自体のSHA-256
- [scripts/verify_pack.py](scripts/verify_pack.py) — オフライン整合性検証コード
- [SECURITY.md](SECURITY.md) — 警告表示・安全性と注意点

公開・ハッシュ照合は透明性を高め、ファイル改変の検出に役立ちます。しかし、**第三者によるセキュリティ監査やマルウェア検査の代わりにはなりません**。

## 更新方針

v1.0.0を検証用の固定構成として扱い、MODは原則追加しません。互換性やセキュリティ上必要な修正のみ、新バージョンとして公開します。

第三者MODは各開発者に権利が帰属します。このリポジトリはMOD本体のJARを再配布せず、公式URLのみを参照します。
