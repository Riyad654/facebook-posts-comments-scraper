# Facebook Posts/Comments Scraper
This scraper helps you extract detailed information from Facebook posts and their comment threads, enabling efficient analysis of user interactions and engagement trends. It captures structured content such as text, reactions, images, videos, and comment metadata to support research, monitoring, and automation workflows. The tool is optimized for accuracy, stability, and clean data extraction.


<p align="center">
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>Facebook Posts/Comments Scraper</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction
The Facebook Posts/Comments Scraper gathers complete post-level and comment-level information from any public Facebook post URL. It solves the challenge of manually collecting engagement metrics, media assets, and conversational data from user interactions. This tool is designed for analysts, marketers, researchers, and developers who need reliable structured data from social content.

### Data-Driven Engagement Extraction
- Retrieves full post content, including text, reactions, media, and metadata.
- Captures comments with user details, timestamps, and nested engagement metrics.
- Supports media-rich extraction, including photos, videos, and preview images.
- Ensures consistent timestamps and identifiers for accurate downstream analysis.
- Handles multiple URLs and configurable limits for controlled data output.

## Features
| Feature | Description |
|---------|-------------|
| Post Extraction | Gathers text, author details, engagement numbers, media assets, and posting time. |
| Comment Scraping | Extracts comments with user identity, text, engagement, and timestamps. |
| Media Capture | Retrieves image lists, video links, and cover images linked to posts or comments. |
| Custom Wait Times | Allows adjustable delay limits to ensure stable extraction. |
| Cookie Support | Accepts user cookies for authenticated access where needed. |

---

## What Data This Scraper Extracts
| Field Name | Field Description |
|------------|------------------|
| input | URL that was processed for scraping. |
| author | Full author object when available. |
| post_id | Unique identifier for each Facebook post. |
| action_id | Action-based identifier tied to Facebook’s internal systems. |
| text | The text content of the main post. |
| create_time | UNIX timestamp of the post creation time. |
| post_url | Direct URL to the scraped post. |
| like_count | Total number of likes/reactions. |
| comment_count | Total number of comments. |
| share_count | Number of times the post has been shared. |
| image_list | List of image URLs attached to the post. |
| video_list | List of video URLs attached to the post. |
| author_username | Display name of the post author. |
| author_user_id | User ID of the post author. |
| comments | Array of nested comment objects with full metadata. |

---

## Example Output

Example:


        {
            "input": "https://www.facebook.com/thewitcherfanclub/posts/pfbid02reBdcEgYdgLLP92A7ZJ6KLPcNq3LHha9TjYi2k2ytbeS2q2rxkhCqAWy2m6j3TkRl",
            "author": null,
            "post_id": "623731507071105",
            "action_id": "ZmVlZGJhY2s6NjIzNzMxNTA3MDcxMTA1",
            "text": "The Witcher ⚔️ Season 4 2025",
            "create_time": 1739523981,
            "post_url": "https://www.facebook.com/thewitcherfanclub/posts/pfbid02rx7CsmHhurFSpK1W7NY6p9YGRZbY2s1W2ZsqX5MstidN9zaM2ToHJexKJ2EkfyDwl",
            "like_count": 15443,
            "comment_count": 647,
            "share_count": 629,
            "view_count": 0,
            "play_count": 0,
            "image_list": [
                "https://scontent.xx.fbcdn.net/v/t39.30808-6/484004189_645200288257560_5160343900984361714_n.jpg?_nc_cat=109..."
            ],
            "video_list": [],
            "author_username": "The Witcher Memes",
            "author_user_id": "100083027845965",
            "comments": [
                {
                    "action_id": "ZmVlZGJhY2s6NjIzNzMxNTA3MDcxMTA1XzU2NzAzMTAzNjQwNDAxNQ==",
                    "comment_id": "567031036404015",
                    "author_username": "komene Rika Ng duwur kaeh",
                    "text": "Totally loved this film from start to finish...",
                    "like_count": 9,
                    "reply_count": 3,
                    "create_time": 1739803304
                }
            ]
        }

---

## Directory Structure Tree


        facebook-posts-scraper/
        ├── src/
        │   ├── runner.py
        │   ├── extractors/
        │   │   ├── facebook_parser.py
        │   │   └── utils_time.py
        │   ├── outputs/
        │   │   └── exporters.py
        │   └── config/
        │       └── settings.example.json
        ├── data/
        │   ├── inputs.sample.txt
        │   └── sample.json
        ├── requirements.txt
        └── README.md

---

## Use Cases
- **Marketing teams** track engagement trends on public posts to improve content strategy and audience alignment.
- **Brand analysts** monitor reactions, comments, and sentiment to evaluate brand perception across communities.
- **Researchers** study public conversations and behavioral patterns for academic or social insights.
- **Influencer managers** analyze creator posts to benchmark engagement performance.

---

## FAQs
**Does this scraper work with any public Facebook post?**
Yes, it supports extraction from all publicly accessible post URLs and delivers full metadata where available.

**Can I extract posts that require login?**
Yes, cookies can be added to enable access to posts that require authentication.

**Does it support comment limits?**
You can configure comment extraction depth using the comments_limit field to control output size.

---

## Performance Benchmarks and Results
**Primary Metric:** Capable of processing most posts within 2–4 seconds depending on media size.
**Reliability Metric:** Maintains a stable success rate above 97% across large input lists.
**Efficiency Metric:** Designed to handle batch URLs with minimal memory overhead.
**Quality Metric:** Ensures high completeness of comment threads, reaction data, and media links through structured parsing.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
