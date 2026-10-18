# 安全性の説明（配信者・参加者向け）

> [!WARNING]
> **VDESK WORLDのこの独自MODパックは、Modrinth内で公開・審査されていません。**
>
> そのため **Unknown file warning** が出ます。**警告はウイルス検出を意味しませんが、安全であることも保証しません。**

GitHub公開は出所と内容を確認しやすくするための措置です。「GitHubにあるから安全」「MODがModrinthにあるから安全」という保証はできません。

### 確認できること

- MOD29件の個別プロジェクトページは [MODS.md](MODS.md) で確認できます。
- 取得元URLはすべて `cdn.modrinth.com` のHTTPSです。
- 配布ファイルのSHA-256は [SHA256SUMS.txt](SHA256SUMS.txt) で検証できます。
- 取得予定の各JARのSHA-1/SHA-512は [manifest.json](manifest.json) で確認できます。
- .mrpack とmanifestの一致は [scripts/verify_pack.py](scripts/verify_pack.py) で確認できます（マルウェア検査ではありません）。
- 本リポジトリにJARファイルや独立のインストーラ/実行ファイルを同梱しません。

### インストールする方へ

出所・警告・導入の必要性を理解できない場合は **Don't install** を選択して構いません。警告の非表示設定を有効にする必要もありません。入れる場合は既存の環境とは別のプロファイルを使用してください。

本番サーバー情報・配信者の個人情報・認証情報・未公開イベントのデータはこのリポジトリには含まれません。
