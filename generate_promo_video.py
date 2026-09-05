#!/usr/bin/env python3
"""
=============================================================================
KL_BEAUTY OREOKASTRO - Promo Video Generator
ΞΞΉΞ±ΟΞ·ΞΌΞΉΟΟΞΉΞΊΟ Ξ²Ξ―Ξ½ΟΞ΅ΞΏ ΟΟΞ·Ξ»Ξ�Ο Ξ±Ξ½Ξ¬Ξ»ΟΟΞ·Ο (Vertical 1080x1920 Ξ³ΞΉΞ± Reels / TikTok / Shorts)
- ΞΟΟΞ�: ΞΟΟΟΞ΅ΟΞΉΞΊΟ ΟΞ±Ξ»ΞΏΞ½ΞΉΞΏΟ ΞΌΞ΅ ΟΟΟΞΉΞΆΟΞΌΞ΅Ξ½Ξ΅Ο ΞΊΞ±ΞΌΞ¬ΟΞ΅Ο
- Ξ₯ΟΞ·ΟΞ΅ΟΞ―Ξ΅Ο: ΞΟΞ½ΞΏ ΟΞ­ΟΞΉΞ± (ΞΞ±Ξ»Ξ»ΞΉΞ¬, ΞΟΟΞΉΞ±, ΞΞ±ΞΊΞΉΞ³ΞΉΞ¬ΞΆ - ΟΟΟΞ―Ο ΟΟΟΟΟΟΞ±)
- Ξ€Ξ­Ξ»ΞΏΟ: Ξ£ΟΞΏΞΉΟΞ΅Ξ―Ξ± Ξ΅ΟΞΉΞΊΞΏΞΉΞ½ΟΞ½Ξ―Ξ±Ο (ΞΞ΅ΟΟΟΟΞΏΟ ΞΞ·ΞΌΞΏΞΊΟΞ±ΟΞ―Ξ±Ο 31, Ξ€Ξ·Ξ»: 6975659830)
=============================================================================
"""

import math
import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1080, 1920
FPS = 30
OUTPUT_FILENAME = "kl_beauty_promo.mp4"

# ΞΟΞΉΞ»ΞΏΞ³Ξ� Ξ³ΟΞ±ΞΌΞΌΞ±ΟΞΏΟΞ΅ΞΉΟΞ¬Ο ΟΟΟΟΞ�ΞΌΞ±ΟΞΏΟ
FONT_TITLE_PATH = "/usr/share/fonts/GoogleSans-Regular.ttf"
if not os.path.exists(FONT_TITLE_PATH):
    FONT_TITLE_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

def get_font(size):
    try:
        return ImageFont.truetype(FONT_TITLE_PATH, size)
    except Exception:
        return ImageFont.load_default()

def draw_text_centered(draw, text, y, font, fill=(255, 255, 255), shadow=True):
    bbox = font.getbbox(text)
    w = bbox[2] - bbox[0]
    x = (WIDTH - w) // 2
    if shadow:
        draw.text((x + 2, y + 2), text, font=font, fill=(20, 15, 12, 200))
    draw.text((x, y), text, font=font, fill=fill)

def create_gradient(color_top, color_bottom, w=WIDTH, h=HEIGHT):
    img = np.zeros((h, w, 3), dtype=np.uint8)
    for c in range(3):
        img[:, :, c] = np.linspace(color_top[c], color_bottom[c], h, dtype=np.uint8)[:, None]
    return img

# 1. Ξ£ΞΊΞ·Ξ½Ξ� 1: Ξ€ΞΏ Ξ΅ΟΟΟΞ΅ΟΞΉΞΊΟ ΟΞΏΟ ΞΌΞ±Ξ³Ξ±ΞΆΞΉΞΏΟ ΞΌΞ΅ ΟΞΉΟ ΟΟΟΞΉΞΆΟΞΌΞ΅Ξ½Ξ΅Ο ΞΊΞ±ΞΌΞ¬ΟΞ΅Ο (Arched Mirrors)
def render_salon_arch_scene(progress):
    base = create_gradient((28, 24, 26), (65, 52, 48))
    img = Image.fromarray(base)
    draw = ImageDraw.Draw(img, "RGBA")
    
    zoom = 1.0 + 0.08 * progress
    arch_centers = [WIDTH // 4, WIDTH // 2, 3 * WIDTH // 4]
    arch_w = int(220 * zoom)
    arch_h = int(600 * zoom)
    arch_y = int(550 - 30 * progress)
    
    for ax in arch_centers:
        left = ax - arch_w // 2
        right = ax + arch_w // 2
        top = arch_y
        bottom = arch_y + arch_h
        
        # ΞΞ΅ΟΟΟ glow ΟΟΟΞΉΟΞΌΞΏΟ LED
        for g in range(12, 0, -3):
            draw.rounded_rectangle([left - g, top - g, right + g, bottom + g], radius=arch_w//2 + g,
                                  outline=(235, 195, 140, 25), width=3)
        
        # ΞΞ±ΞΈΟΞ­ΟΟΞ·Ο ΞΊΞ±ΞΌΞ¬ΟΞ±Ο
        draw.rounded_rectangle([left, top, right, bottom], radius=arch_w//2,
                              fill=(45, 40, 42, 230), outline=(230, 190, 140, 255), width=4)
        
        # ΞΞ½Ξ¬ΞΊΞ»Ξ±ΟΞ· ΟΟΟΟΟ
        draw.line([left + 30, top + 80, left + 40, bottom - 50], fill=(255, 230, 200, 70), width=6)
        
        # ΞΞ­ΟΞ· ΞΊΞ±ΟΞ­ΞΊΞ»Ξ±Ο
        chair_y = bottom - 80
        draw.ellipse([ax - 45, chair_y, ax + 45, chair_y + 90], fill=(25, 20, 22, 220))
        draw.rectangle([ax - 35, chair_y + 40, ax + 35, chair_y + 160], fill=(30, 25, 28, 220))

    font_sub = get_font(38)
    font_main = get_font(64)
    font_loc = get_font(36)
    
    draw_text_centered(draw, "ΞΞΞΞ©Ξ£ ΞΞ‘ΞΞΞ€Ξ Ξ£Ξ€ΞΞ Ξ§Ξ©Ξ‘Ξ ΞΞΞ£", int(320 - 20 * progress), font_sub, (215, 180, 140))
    draw_text_centered(draw, "KL_BEAUTY", int(380 - 20 * progress), font_main, (255, 255, 255))
    draw_text_centered(draw, "OREOKASTRO", int(460 - 20 * progress), font_sub, (230, 195, 150))
    draw_text_centered(draw, "ΞΞ»ΞΏΞΊΞ»Ξ·ΟΟΞΌΞ­Ξ½Ξ· Ξ Ξ΅ΟΞΉΟΞΏΞ―Ξ·ΟΞ· & ΞΞΉΟΞΈΞ·ΟΞΉΞΊΞ�", 1520, font_loc, (240, 230, 220))
    
    return np.array(img.convert("RGB"))

# 2. Ξ£ΞΊΞ·Ξ½Ξ� 2: Ξ§Ξ­ΟΞΉΞ± ΟΞΏΟ ΟΟΞ΅Ξ½Ξ―ΞΆΞΏΟΞ½ ΞΌΞ±Ξ»Ξ»ΞΉΞ¬ (Ξ§ΟΟΞ―Ο ΟΟΟΟΟΟΞΏ)
def render_hair_scene(progress):
    base = create_gradient((35, 28, 25), (75, 55, 45))
    img = Image.fromarray(base)
    draw = ImageDraw.Draw(img, "RGBA")
    
    offset = int(math.sin(progress * math.pi * 3) * 25)
    hair_color = (185, 145, 95)
    hair_dark = (130, 95, 60)
    for wave in range(-4, 5):
        wx = WIDTH // 2 + wave * 45
        for seg in range(12):
            sy = 650 + seg * 70
            sx = wx + int(math.sin(seg * 0.6 + progress * 2) * 35)
            draw.ellipse([sx - 38, sy - 38, sx + 38, sy + 38], fill=hair_dark)
            draw.ellipse([sx - 37, sy - 37, sx + 27, sy + 27], fill=hair_color)

    # Ξ§Ξ­ΟΞΉΞ± ΞΊΞΏΞΌΞΌΟΟΟΞΉΞ±Ο ΟΞΏΟ ΞΊΞ¬Ξ½ΞΏΟΞ½ styling
    draw.polygon([(180, 1200), (320, 980), (380, 920), (450, 950), (400, 1060), (250, 1300)], fill=(215, 175, 145))
    draw.polygon([(900, 1200), (760, 950), (690, 890), (640, 930), (700, 1040), (830, 1300)], fill=(210, 170, 140))
    
    # Ξ§ΟΞ­Ξ½Ξ± styling
    draw.line([620, 870, 710, 960], fill=(240, 200, 120), width=14)
    for t in range(7):
        draw.line([640 + t*10, 890 + t*10, 625 + t*10, 915 + t*10], fill=(240, 200, 120), width=3)
        
    font_tag = get_font(42)
    font_desc = get_font(56)
    draw_text_centered(draw, "Ξ₯Ξ ΞΞ‘ΞΞ£ΞΞΞ£ ΞΞΞΞΞ©Ξ€ΞΞ‘ΞΞΞ₯", 320, font_tag, (230, 195, 150))
    draw_text_centered(draw, "ΞΞΎΞ΅ΞΉΞ΄ΞΉΞΊΞ΅ΟΞΌΞ­Ξ½ΞΏ Styling & ΞΞ΅ΟΞ±ΟΞ΅Ξ―Ξ΅Ο", 400, font_desc, (255, 255, 255))
    draw_text_centered(draw, "ΞΞΏΟΟΞ΅ΞΌΞ± β’ Ξ§ΟΞ­Ξ½ΞΉΟΞΌΞ± β’ ΞΞ±ΟΞ� β’ Balayage", 1520, font_tag, (220, 210, 200))
    
    return np.array(img.convert("RGB"))

# 3. Ξ£ΞΊΞ·Ξ½Ξ� 3: Ξ§Ξ­ΟΞΉΞ± ΟΞΏΟ ΞΊΞ¬Ξ½ΞΏΟΞ½ Ξ½ΟΟΞΉΞ± (ΞΞ±Ξ½ΞΉΞΊΞΉΞΏΟΟ / Nail Art)
def render_nails_scene(progress):
    base = create_gradient((40, 25, 35), (80, 50, 65))
    img = Image.fromarray(base)
    draw = ImageDraw.Draw(img, "RGBA")
    
    brush_move = int(math.sin(progress * math.pi * 4) * 20)
    
    # Ξ§Ξ­ΟΞΉ ΟΞ΅Ξ»Ξ¬ΟΞΉΟΟΞ±Ο
    draw.rectangle([WIDTH//2 - 90, 800, WIDTH//2 + 90, 1350], fill=(225, 185, 160))
    finger_x = [WIDTH//2 - 80, WIDTH//2 - 40, WIDTH//2, WIDTH//2 + 40, WIDTH//2 + 80]
    for idx, fx in enumerate(finger_x):
        fy = 720 - (15 if idx in [1,2] else 0)
        draw.rounded_rectangle([fx - 16, fy, fx + 16, 840], radius=16, fill=(225, 185, 160))
        draw.rounded_rectangle([fx - 12, fy + 4, fx + 12, fy + 38], radius=10, fill=(230, 155, 150), outline=(255, 220, 210), width=2)
        draw.ellipse([fx - 6, fy + 8, fx - 2, fy + 18], fill=(255, 255, 255, 200))

    # Ξ§Ξ­ΟΞΉ ΞΌΞ±Ξ½ΞΉΞΊΞΉΞΏΟΟΞ―ΟΟΞ±Ο & Ξ»Ξ΅ΟΟΟ ΟΞΉΞ½Ξ­Ξ»ΞΏ
    brush_x = WIDTH//2 + brush_move
    brush_y = 690
    draw.line([brush_x + 120, brush_y - 120, brush_x + 5, brush_y + 25], fill=(210, 180, 120), width=10)
    draw.polygon([(brush_x, brush_y + 32), (brush_x + 12, brush_y + 20), (brush_x + 2, brush_y + 15)], fill=(240, 130, 130))
    draw.polygon([(WIDTH//2 + 100, 520), (WIDTH//2 + 250, 420), (WIDTH//2 + 350, 580), (WIDTH//2 + 180, 680)], fill=(218, 178, 152))

    font_tag = get_font(42)
    font_desc = get_font(56)
    draw_text_centered(draw, "Ξ ΞΞ‘ΞΞ ΞΞΞΞ£Ξ ΞΞΞ‘Ξ©Ξ", 320, font_tag, (230, 195, 150))
    draw_text_centered(draw, "ΞΞ±Ξ½ΞΉΞΊΞΉΞΏΟΟ β’ Gel β’ Nail Art", 400, font_desc, (255, 255, 255))
    draw_text_centered(draw, "ΞΟΟΞ»ΟΟΞ· Ξ±Ξ½ΟΞΏΟΞ� & Ξ¬ΟΞΏΞ³Ξ· Ξ±ΞΉΟΞΈΞ·ΟΞΉΞΊΞ�", 1520, font_tag, (220, 210, 200))
    
    return np.array(img.convert("RGB"))

# 4. Ξ£ΞΊΞ·Ξ½Ξ� 4: Ξ§Ξ­ΟΞΉΞ± ΟΞΏΟ ΞΊΞ¬Ξ½ΞΏΟΞ½ ΞΌΞ±ΞΊΞΉΞ³ΞΉΞ¬ΞΆ ΞΌΞ΅ ΟΞΉΞ½Ξ­Ξ»ΞΏ
def render_makeup_scene(progress):
    base = create_gradient((30, 28, 38), (65, 55, 75))
    img = Image.fromarray(base)
    draw = ImageDraw.Draw(img, "RGBA")
    
    offset_x = int(math.sin(progress * math.pi * 3.5) * 35)
    offset_y = int(math.cos(progress * math.pi * 3.5) * 20)
    
    # ΞΟΞ­ Ξ»Ξ¬ΞΌΟΞ·Ο & ΟΟΞΌΞ±ΟΞΉΞ΄Ξ―ΟΞ½
    for p in range(40):
        ang = (p / 40.0) * math.pi * 2 + progress * 2
        dist = 90 + (p * 5) % 110
        px = WIDTH // 2 + offset_x + int(math.cos(ang) * dist)
        py = 820 + offset_y + int(math.sin(ang) * dist)
        draw.ellipse([px-4, py-4, px+4, py+4], fill=(245, 215, 170, 160))

    # Ξ ΞΉΞ½Ξ­Ξ»ΞΏ ΞΞ±ΞΊΞΉΞ³ΞΉΞ¬ΞΆ & Ξ§Ξ­ΟΞΉ
    brush_tip_x = WIDTH // 2 + offset_x
    brush_tip_y = 820 + offset_y
    draw.polygon([(brush_tip_x, brush_tip_y), (brush_tip_x + 55, brush_tip_y - 70), (brush_tip_x + 95, brush_tip_y - 45)], fill=(45, 40, 42))
    draw.polygon([(brush_tip_x + 55, brush_tip_y - 70), (brush_tip_x + 95, brush_tip_y - 45), (brush_tip_x + 130, brush_tip_y - 90), (brush_tip_x + 90, brush_tip_y - 115)], fill=(235, 195, 120))
    draw.polygon([(brush_tip_x + 110, brush_tip_y - 100), (brush_tip_x + 360, brush_tip_y - 400), (brush_tip_x + 385, brush_tip_y - 380), (brush_tip_x + 135, brush_tip_y - 80)], fill=(25, 20, 22))
    draw.polygon([(brush_tip_x + 240, brush_tip_y - 250), (brush_tip_x + 460, brush_tip_y - 380), (brush_tip_x + 520, brush_tip_y - 280), (brush_tip_x + 300, brush_tip_y - 170)], fill=(218, 178, 150))

    font_tag = get_font(42)
    font_desc = get_font(56)
    draw_text_centered(draw, "ΞΞ ΞΞΞΞΞΞΞΞ€ΞΞΞ ΞΞΞΞΞΞΞΞ", 320, font_tag, (230, 195, 150))
    draw_text_centered(draw, "ΞΟΟΞΉΞΊΟ β’ ΞΟΞ±Ξ΄ΞΉΞ½Ο β’ Glam Look", 400, font_desc, (255, 255, 255))
    draw_text_centered(draw, "ΞΞ½Ξ¬Ξ΄Ξ΅ΞΉΞΎΞ· ΟΟΞ½ ΟΟΟΞΉΞΊΟΞ½ ΟΞ±Ο Ξ³ΟΞ±ΞΌΞΌΟΞ½", 1520, font_tag, (220, 210, 200))
    
    return np.array(img.convert("RGB"))

# 5. Ξ£ΞΊΞ·Ξ½Ξ� 5: Ξ€Ξ΅Ξ»ΞΉΞΊΞ� ΞΞ¬ΟΟΞ± ΞΌΞ΅ ΟΞ± ΟΟΞΏΞΉΟΞ΅Ξ―Ξ± ΟΞΏΟ ΞΌΞ±Ξ³Ξ±ΞΆΞΉΞΏΟ
def render_end_card(progress):
    base = create_gradient((20, 18, 20), (50, 42, 40))
    img = Image.fromarray(base)
    draw = ImageDraw.Draw(img, "RGBA")
    
    pad = 50
    draw.rectangle([pad, pad, WIDTH - pad, HEIGHT - pad], outline=(215, 175, 130), width=3)
    draw.rectangle([pad + 12, pad + 12, WIDTH - pad - 12, HEIGHT - pad - 12], outline=(180, 140, 100, 120), width=1)
    
    for cx, cy in [(pad, pad), (WIDTH-pad, pad), (pad, HEIGHT-pad), (WIDTH-pad, HEIGHT-pad)]:
        draw.rectangle([cx - 8, cy - 8, cx + 8, cy + 8], fill=(230, 190, 140))

    font_title = get_font(72)
    font_city = get_font(46)
    font_sub = get_font(38)
    font_info_title = get_font(34)
    font_info_val = get_font(48)
    font_cta = get_font(40)

    pulse = int(math.sin(progress * math.pi * 2) * 5)
    
    draw_text_centered(draw, "KL_BEAUTY", 380, font_title, (255, 255, 255))
    draw_text_centered(draw, "OREOKASTRO", 480, font_city, (230, 190, 140))
    draw_text_centered(draw, "ΞΞΞΞΞ©Ξ€ΞΞ‘ΞΞ β’ ΞΞ₯Ξ§ΞΞ β’ ΞΞΞΞΞΞΞΞ", 570, font_sub, (210, 200, 195))
    
    draw.line([WIDTH//2 - 200, 660, WIDTH//2 + 200, 660], fill=(215, 175, 130), width=2)
    
    # ΞΞΉΞ΅ΟΞΈΟΞ½ΟΞ·
    draw_text_centered(draw, "ΞΞΞΞ₯ΞΞ₯ΞΞ£Ξ", 820, font_info_title, (200, 170, 140))
    draw_text_centered(draw, "ΞΞ΅ΟΟΟΟΞΏΟ ΞΞ·ΞΌΞΏΞΊΟΞ±ΟΞ―Ξ±Ο 31", 880, font_info_val, (255, 255, 255))
    draw_text_centered(draw, "Ξ©ΟΞ±ΞΉΟΞΊΞ±ΟΟΟΞΏ, ΞΞ΅ΟΟΞ±Ξ»ΞΏΞ½Ξ―ΞΊΞ·", 950, font_city, (220, 210, 200))
    
    # Ξ€Ξ·Ξ»Ξ­ΟΟΞ½ΞΏ
    draw_text_centered(draw, "Ξ€ΞΞΞΞ¦Ξ©ΞΞ Ξ‘ΞΞΞ€ΞΞΞΞ₯", 1120, font_info_title, (200, 170, 140))
    draw_text_centered(draw, "6975 659 830", 1180, font_info_val, (245, 210, 160))
    
    # ΞΞΏΟΞΌΟΞ― Call-to-action
    btn_w, btn_h = 600, 95
    bx1 = (WIDTH - btn_w) // 2
    by1 = 1400 + pulse
    draw.rounded_rectangle([bx1, by1, bx1 + btn_w, by1 + btn_h], radius=45, fill=(215, 165, 115), outline=(255, 235, 205), width=2)
    draw_text_centered(draw, "ΞΞΞΞΞ£Ξ€Ξ Ξ€Ξ Ξ‘ΞΞΞ€ΞΞΞΞ₯ Ξ£ΞΞ£", by1 + 24, font_cta, (25, 20, 22), shadow=False)
    
    return np.array(img.convert("RGB"))

def build_promo_video():
    scenes = [
        ("salon", render_salon_arch_scene, 3.5),
        ("hair", render_hair_scene, 3.0),
        ("nails", render_nails_scene, 3.0),
        ("makeup", render_makeup_scene, 3.0),
        ("end", render_end_card, 4.0),
    ]
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(OUTPUT_FILENAME, fourcc, FPS, (WIDTH, HEIGHT))
    
    transition_frames = int(FPS * 0.4) # Crossfade 0.4 sec
    prev_last_frame = None
    
    for name, render_func, duration in scenes:
        total_frames = int(duration * FPS)
        print(f"ΞΞ·ΞΌΞΉΞΏΟΟΞ³Ξ―Ξ± ΟΞΊΞ·Ξ½Ξ�Ο: {name} ({total_frames} frames)...")
        
        for f in range(total_frames):
            prog = f / float(total_frames)
            current_frame = render_func(prog)
            
            if prev_last_frame is not None and f < transition_frames:
                alpha = f / float(transition_frames)
                blended = cv2.addWeighted(prev_last_frame, 1.0 - alpha, current_frame, alpha, 0)
                frame_bgr = cv2.cvtColor(blended, cv2.COLOR_RGB2BGR)
            else:
                frame_bgr = cv2.cvtColor(current_frame, cv2.COLOR_RGB2BGR)
                
            out.write(frame_bgr)
            
        prev_last_frame = render_func(1.0)
        
    out.release()
    print(f"Ξ€ΞΏ Ξ²Ξ―Ξ½ΟΞ΅ΞΏ Ξ΄Ξ·ΞΌΞΉΞΏΟΟΞ³Ξ�ΞΈΞ·ΞΊΞ΅ Ξ΅ΟΞΉΟΟΟΟΟ: {OUTPUT_FILENAME}")

if __name__ == "__main__":
    build_promo_video()
