"""
browser-harness PoC: 对比 MediaCrawler 现有 CDP 实现
检查 MediaCrawler 的 CDPBrowserManager 和 browser-harness 的差异
"""
import sys
sys.path.insert(0, "/home/haha/workspace/codespace/MediaCrawler")

# 检查 MediaCrawler 的 CDP 实现结构
from tools.cdp_browser import CDPBrowserManager
import inspect

print("=== MediaCrawler CDPBrowserManager 方法列表 ===")
for name, method in inspect.getmembers(CDPBrowserManager, predicate=inspect.isfunction):
    if not name.startswith('_'):
        sig = inspect.signature(method)
        print(f"  {name}{sig}")

print("\n=== 关键特性对比 ===")
print("MediaCrawler CDP:")
print("  - 基于 Playwright async_api")
print("  - 手动管理 browser 进程生命周期（atexit + signal）")
print("  - 支持连接已有浏览器 OR 自动启动")
print("  - 有 stealth.min.js 反检测注入")
print("  - 手动管理 context/page")

print("\nbrowser-harness (browser-use):")
print("  - 基于 cdp-use（Rust CDP client）")
print("  - 自愈机制：操作失败自动重试 + patch")
print("  - 持久化 session（cookie/login 保持跨任务）")
print("  - LLM 原生驱动（自然语言 → 浏览器操作）")
print("  - 更轻量（不需要 Playwright 完整依赖）")

print("\n=== 接入建议 ===")
print("MediaCrawler 的爬虫模式是「固定 selector + 循环翻页」，")
print("browser-harness 的优势在「自愈」和「LLM 理解页面变化」。")
print("最适合接入的场景：小红书/抖音等反爬严格的平台，")
print("页面结构频繁变化导致 selector 失效 → browser-harness 自动适应。")
print("微博/知乎/贴吧等结构稳定的平台 → 现有 CDP 方案够用。")
