## [标识符-matplotlib.markers](https://matplotlib.org/stable/api/markers_api.html)

可以在绘图函数内通过`marker="marker name"`设置标识符，
标识符大小通过`markersize1=<16>`设置。下面是一些常用的`marker name`


|marker|symbol|description|
|-|-|-|
|"."|![point](image/m00.webp)|point|
|","|![pixel](image/m01.webp)|pixel|
|"o"|![circle](image/m02.webp)|circle|
|"v"|![triangle_down](image/m03.webp)|triangle_down|
|"^"|![triangle_up](image/m04.webp)|triangle_up|
|"<"|![triangle_left](image/m05.webp)|triangle_left|
|">"|![triangle_right](image/m06.webp)|triangle_right|
|"1"|![tri_down](image/m07.webp)|tri_down|
|"2"|![tri_up](image/m08.webp)|tri_up|
|"3"|![tri_left](image/m09.webp)|tri_left|
|"4"|![tri_right](image/m10.webp)|tri_right|
|"8"|![octagon](image/m11.webp)|octagon|
|"s"|![square](image/m12.webp)|square|
|"p"|![pentagon](image/m13.webp)|pentagon|
|"P"|![plus(filled)](image/m23.webp)|plus(filled)|
|"*"|![star](image/m14.webp)|star|
|"h"|![hexagon1](image/m15.webp)|hexagon1|
|"H"|![hexagon2](image/m16.webp)|hexagon2|
|"+"|![plus](image/m17.webp)|plus|
|"x"|![x](image/m18.webp)|x|
|"X"|![x(filled)](image/m24.webp)|x(filled)|
|"D"|![diamond](image/m19.webp)|diamond|
|"d"|![thin_diamond](image/m20.webp)|thin_diamond|
|"\|"|![vline](image/m21.webp)|vline|
|"_"|![hline](image/m22.webp)|hline|



## [线形-linestyles](https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html)

线型参数可以通过`linestyle="linestyle name"`设置，
线宽控制为`linewidth=<2>` or `lw=<2>`
常用的`linestyle name`为
+ `solid` 实线
+ `dotted` 点线
+ `dashed` 虚线
+ `dashdot` 点画线

线形还可以通过一个元组`(a, (b,c,...))`控制，其中
+ `a`: 线条的重复方式，通常为0
+ `b`: 线段长度
+ `c`: 空白长度
+ `d`: 下一段线长度(可选)
+ `e`: 下一段空白长度(可选)

下面是一些效果
![linestyle](image/linestyle.png)


## [颜色-matplotlib.colors](https://matplotlib.org/stable/gallery/color/named_colors.html)

颜色的控制参数为`color="color name"`，`color name`有很多形式，包括
1. 单字母：
![单字颜色](image/named_colors_2.jpg)
2. 单词：
![单词颜色](image/named_colors_1.jpg)
3. 六位十六进制颜色值

+ <font color="#ff0094">#ff0094</font>
+ <font color="#ff0000">#ff0000</font>
+ <font color="#000000">#000000</font>

## [颜色映射-colormap](https://matplotlib.org/stable/gallery/color/colormap_reference.html)

颜色映射的控制参数为`cmap="colormap name"`，常用的`colormap name`为

+ `jet`: `ANSYS Fluent`默认选项
+ `coolwarm`: `Paraview`默认选项
+ `hot`: `Comsol`默认选项
+ `Greys` or `gray`: 灰度
+ `binary`: 黑白二值

![](image/cmap_7.jpg)
![](image/cmap_1.jpg)
![](image/cmap_2.jpg)
![](image/cmap_3.jpg)
![](image/cmap_4.jpg)
![](image/cmap_5.jpg)
![](image/cmap_6.jpg)

