尝试直接从原图搜索特定几种颜色，用作ui的颜色。

使用adobe color cc

https://color.adobe.com/zh/create/image, 可以从上传的图片中寻找一些色彩。

# ref

不需要的样式其实可以删掉, 各个区块无css样式则使用主题色填充。

## index.css
```css
:root {
--primaryColor: #f17d34; // 主色调
--backgroundColor: #fdfdfd; // 背景色
--dividerColor: rgba(0, 0, 0, 0.1); // 分割线颜色
--listHoverColor: rgba(0, 0, 0, 0.05); // 列表悬浮颜色
--listActiveColor: rgba(0, 0, 0, 0.1); // 列表选中颜色
--textColor: #333333; // 主文本颜色
--maskColor: rgba(51, 51, 51, 0.2); // 遮罩层颜色
--shadowColor: rgba(0, 0, 0, 0.2); // 对话框等阴影颜色
/** --shadow:  // shadow属性 */
--placeholderColor: #f4f4f4; // 输入区背景颜色
--successColor: #08A34C; // 成功颜色
--dangerColor: #FC5F5F; // 危险颜色
--infoColor: #0A95C8; // 通知颜色
--headerTextColor: white; // 顶部文本颜色
--backdropColor: #ffffff !important;//弹窗等地方的背景颜色，默认和背景色一致*/

}

.header-container {
background-color: #97D9E1; //顶部区颜色

.music-bar-container {
  background-color: #D9AFD9 !important;//底部栏颜色
}

.body-container {
  background-color: rgba(0, 0, 0, 0.15);//中间主体颜色，独立于背景色
}

/*音乐详情页背景*/
.music-detail-background {
background-image: linear-gradient(0deg, #D9AFD9 0%, #97D9E1 100%) !important;
mask-image: none !important;
-webkit-mask-image: none !important;
}

.components--tag-container { //标签背景
    background-color: transparent !important;
}

.side-bar-container {
    background-color: black !important; //左侧边栏
}

}
```

## config.json
```json
{
    "name": "主题包的名称",
    "preview": "#000000", // 预览图，支持颜色或图片；
    "description": "描述文本",
    "iframes": {
        "app": "http://musicfree.upup.fun", // 整个软件的背景
        "header": "", // 头部区域的背景
        "body": "", // 侧边栏+主页面区域的背景
        "side-bar": "", // 侧边栏区域的背景
        "page": "", // 主页面区域的背景
        "music-bar": "", // 底部音乐栏的背景

    }
}
```
## 关于preview

说起来每次更改css都会涉及ui的改变，那每一次都修改preview.png实在是麻烦，不如以后把背景改成单纯网页或者背景图片的截图，这样就不用反复修改了