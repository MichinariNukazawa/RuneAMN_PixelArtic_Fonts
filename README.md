RuneAMN PixelArtic Fonts. ドット絵風ルーン文字フォント
====

#概要
RuneAMN PixelArtic Fontsは、商用イラスト・デザイン向けルーン文字フォントである[RuneAMN_Pro Series Fonts][ghpages_RuneAMN_Pro]の、ドット絵風バリエーションです。  
本プロジェクトでは、[project daisy bell][pixiv_booth_project_daisy_bell]がリリースしている商用フォント製品およびフリーフォントで使っているビルドスクリプトを公開しています。  


## RuneAMN PixelArtic Fontsの特徴:  
 * ドット絵およびPixelArt、レトロゲーム風の外観
 * [RuneAMN_Pro Series Fonts][ghpages_RuneAMN_Pro]と同じ、デザインへの使いやすさ


## 姉妹フォント
[RuneAMN_Pro Series Fonts][ghpages_RuneAMN_Pro] (商用フォント)  
[RuneAMN_Series_Font][ghpages_index_RuneAssignMN_Series_Fonts] (フリーフォント)  
[OlChikiAssignMN_Series_Font][ghpages_index_OlChikiAssignMN_Series_Fonts] (フリーフォント)  
ビルドスクリプトおよび書体ソース画像も、フリーソフトウェアとして公開されています。  


# ライセンス
 [RuneAMN_Pro Series Fonts][ghpages_RuneAMN_Pro]のに準じます。そちらを参照してください。
 ライセンスについて、よくわからない場合は、気軽に作者へ[メール(michinari.nukazawa@gmail.com)][mailto]にて、お問い合わせください。  


#フォント制作手順
本プロジェクトのビルドシステムは、[RuneAMN_Pro Series Fonts][ghpages_RuneAMN_Pro]の生成スクリプトが使用するフォント生成元データを生成します。  
事前に[RuneAMN_Pro Series Fonts][ghpages_RuneAMN_Pro]リポジトリをcloseし、プロジェクトディレクトリ内で以下の通りに操作します。  
`mkdir -p library`  
`cd library`  
`git clone ${THIS_GITHUB_REPOSITORY}`  
`cd ${THIS_REPOSITORY}`  
`make`  
`make movefont`  
以下、[RuneAMN_Pro Series Fonts][ghpages_RuneAMN_Pro]に戻り、ビルドスクリプトを実行します。  


#LICENCE About
Please read Japanese licence text.  
Build script and free fonts design is 2-clause BSD license.  


#連絡先
[michinari.nukazawa@gmail.com][mailto]

Develop by Michinari.Nukazawa, in project "daisy bell".


[pixiv_booth_project_daisy_bell]: https://daisy-bell.booth.pm/
[sourceforge_project_daisy_bell]: http://sourceforge.jp/projects/daisybell-fonts/
[ghpages_RuneAMN_Pro]: http://michinarinukazawa.github.io/RuneAMN_Pro_Series_Fonts/docs/runeamn_pro.html
[typefaces_manuals_pdf]: https://github.com/MichinariNukazawa/RuneAMN_Pro_Series_Fonts/blob/gh-pages/releases/book_of_RuneAMN_Pro_Fonts_limited.pdf?raw=true
[pixiv_nukazawa_index]: http://www.pixiv.net/member.php?id=11951957
[ghpages_index_RuneAssignMN_Series_Fonts]: http://michinarinukazawa.github.io/RuneAssignMN_Series_Fonts/
[ghpages_index_OlChikiAssignMN_Series_Fonts]: http://michinarinukazawa.github.io/OlChikiAssignMN_Series_Fonts/
[blog_article]: http://blog.michinari-nukazawa.com/
[mailto]: mailto:michinari.nukazawa@gmail.com

