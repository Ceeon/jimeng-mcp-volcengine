# 即梦AI MCP服务器 - 火山引擎官方API版

直接调用火山引擎官方API (doubao-seedream-4.0) 的MCP服务器，支持文生图、图生图、多图融合、组图生成等全部功能。

## ✨ 特色功能

- 🎨 **文生图**：根据文字描述生成高质量图像
- 🖼️ **图生图**：基于参考图片生成新图像  
- 🎭 **多图融合**：融合多张参考图的元素（最多10张）
- 📚 **组图生成**：一次生成多张主题相关的图片（最多15张）
- 🚀 **批量处理**：支持多个prompt批量生成
- 💾 **自动保存**：生成的图片自动下载并保存到本地
- 🌐 **官方直连**：直接调用火山引擎官方API，稳定可靠

## 🚀 快速开始

### 1. 克隆仓库
```bash
git clone https://github.com/yourusername/jimeng-mcp-volcengine.git
cd jimeng-mcp-volcengine
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 配置环境变量

```bash
# 复制环境变量模板
cp .env.example .env

# 编辑.env文件，填入您的API密钥
vi .env

# 或者直接设置环境变量
export ARK_API_KEY="your-api-key"
export JIMENG_OUTPUT_DIR="./outputs"
```

### 4. 配置 Claude Desktop

编辑配置文件：
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

添加以下配置：
```json
{
  "mcpServers": {
    "jimeng-volc": {
      "command": "python3",
      "args": ["/path/to/jimeng_mcp.py"],
      "env": {
        "ARK_API_KEY": "your-api-key",
        "JIMENG_OUTPUT_DIR": "~/Desktop/jimeng_images"
      }
    }
  }
}
```

### 5. 重启 Claude Desktop

## 📚 使用示例

### 基础用法

```python
# 简单文生图
jimeng("一只可爱的猫咪在花园里玩耍")

# 指定尺寸
jimeng("壮丽的山水风景画", size="16:9")

# 关闭水印
jimeng("产品图", watermark=False)
```

### 🌟 高级功能

#### 图生图（参考图生成）
```python
# 单张参考图
jimeng("改为卡通风格", image="http://example.com/photo.jpg")

# 多张参考图融合
jimeng(
    prompt="融合这些元素创造新场景",
    image=["url1.jpg", "url2.jpg", "url3.jpg"]
)
```

#### 📚 组图生成（重点！）

组图生成使用`auto`模式，AI会根据prompt内容自动决定生成数量：

```python
# 示例1：生成3张不同时间的图片
jimeng(
    prompt="生成3张不同时间段的海边风景：日出、正午、日落",
    sequential="auto",
    max_images=3  # 设置上限为3张
)

# 示例2：生成5张不同风格
jimeng(
    prompt="生成5张不同艺术风格的花朵：油画、水彩、素描、国画、卡通",
    sequential="auto",
    max_images=5
)

# 示例3：故事叙述
jimeng(
    prompt="生成4张图讲述小猫的一天：起床、吃饭、玩耍、睡觉",
    sequential="auto",
    max_images=4
)
```

**重要提示：**
- 在prompt中明确说明需要的数量（如"生成3张"）
- 详细描述每张图的内容
- `max_images`参数设置为期望的数量

#### 批量生成
```python
# 多prompt批量生成
jimeng(["猫咪", "小狗", "兔子", "仓鼠"])
```

## 📊 参数说明

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `prompt` | str/list | 必需 | 生成描述文本 |
| `image` | str/list | None | 参考图片URL（最多10张） |
| `size` | str | "1:1" | 图片尺寸比例 |
| `watermark` | bool | False | 是否添加水印 |
| `sequential` | str | "disabled" | 组图模式(auto/disabled) |
| `max_images` | int | 15 | 组图最大数量(1-15) |
| `stream` | bool | False | 是否流式传输 |

## 🌐 支持的尺寸

| 比例 | 像素值 | 适用场景 |
|------|--------|----------|
| `1:1` | 2048×2048 | 正方形，社交媒体 |
| `4:3` | 2304×1728 | 横向标准 |
| `3:4` | 1728×2304 | 纵向标准 |
| `16:9` | 2560×1440 | 宽屏，电影 |
| `9:16` | 1440×2560 | 竖屏，手机 |
| `3:2` | 2496×1664 | 横向照片 |
| `2:3` | 1664×2496 | 纵向照片 |
| `21:9` | 3024×1296 | 超宽屏 |

## ⚡ 性能优势

- 支持流式传输，实时返回生成进度
- 动态超时设置，根据任务复杂度调整
- 直连官方API，响应速度快
- 智能错误处理，友好提示信息

## 🔧 火山引擎配置

1. 注册火山引擎账号：https://console.volcengine.com/
2. 开通方舟（Ark）服务
3. 获取API Key
4. 开通 doubao-seedream-4-0-250828 模型

## ⚠️ 注意事项

1. **API限制**
   - 提示词建议≤300汉字或600英文单词
   - 参考图最多10张，每张≤10MB
   - 组图生成：参考图+生成图总数≤15张

2. **图片保存**
   - 默认保存到配置的输出目录
   - URL格式的图片链接24小时后失效
   - 建议及时下载保存

3. **组图生成**
   - 使用auto模式时，在prompt中明确数量
   - 详细描述每张图的变化或特点
   - 合理设置max_images参数

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📝 License

MIT License - 详见 [LICENSE](LICENSE) 文件

## 📧 联系

如有问题或建议，请通过GitHub Issues联系。