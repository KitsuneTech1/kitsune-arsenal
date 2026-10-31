# Kitsune Gateway: small media, file and document utility tools (100 long-tail tools)

Prices are approximate USD per month for the paid product each tool replaces, from general knowledge. No live price checks were run for this list, so every Verified cell says no. Treat all $ figures as rough and re-check before quoting anywhere.

| # | Tool | Does | Replaces | ~$/mo | Backend/method | Verified |
|---|---|---|---|---|---|---|
| 1 | HEIC to JPG/PNG | Convert iPhone HEIC photos to JPG or PNG | CloudConvert, iMazing HEIC | 9 | libheif (heif-convert), pillow-heif | no (approx) |
| 2 | Strip image metadata | Remove EXIF, GPS and XMP from an image | Metadata2Go pro tools | 0 | exiftool, or rebuild from raw pixels with pillow | no (approx) |
| 3 | Read image metadata | Return dimensions, format, DPI, color space, EXIF | none/glue | 0 | imagemagick identify, pillow | no (approx) |
| 4 | Favicon set | Make full favicon and app icon set from one PNG | RealFaviconGenerator (free), Favicon.io | 0 | imagemagick, pillow | no (approx) |
| 5 | Resize to presets | Resize one image to preset sizes (social, store, retina) | Canva Pro resize | 15 | pillow, imagemagick | no (approx) |
| 6 | Smart crop to aspect | Crop to a ratio around the subject | Cloudinary auto-crop | 89 | pillow, smartcrop, opencv saliency | no (approx) |
| 7 | Color palette from image | Extract dominant colors as hex list | Coolors Pro | 5 | pillow k-means, colorthief | no (approx) |
| 8 | Remove background | Cut out subject to transparent PNG | remove.bg | 9 | rembg (U2-Net onnx) | no (approx) |
| 9 | Upscale image | 2x or 4x upscale with detail recovery | Topaz Gigapixel | 17 | Real-ESRGAN ncnn | no (approx) |
| 10 | Compress images | Shrink JPG and PNG with little visible loss | TinyPNG API | 5 | mozjpeg, oxipng, pngquant | no (approx) |
| 11 | Convert to WebP/AVIF | Modern format conversion with quality target | Cloudinary, imgix | 25 | cwebp, avifenc, libvips | no (approx) |
| 12 | SVG to PNG | Rasterize SVG at a chosen size | CloudConvert | 9 | resvg, cairosvg | no (approx) |
| 13 | PNG to SVG trace | Vectorize a logo or bitmap | Vectorizer.ai | 10 | potrace, vtracer | no (approx) |
| 14 | GIF from frames | Build an animated GIF from image frames | ezgif (ad-supported), Giphy Create | 0 | ffmpeg palettegen, imagemagick | no (approx) |
| 15 | Video clip to GIF | Turn a video segment into a small GIF | Gifski app, Kapwing | 16 | ffmpeg palettegen/paletteuse | no (approx) |
| 16 | GIF to MP4/WebM | Convert GIF to compact video | CloudConvert | 9 | ffmpeg | no (approx) |
| 17 | Watermark image | Stamp text or logo at corner or tiled | Watermarkly, Canva | 9 | pillow, imagemagick composite | no (approx) |
| 18 | Redact or blur regions | Blur or box out given rectangles or text matches | Snagit, Skitch | 5 | pillow, opencv, tesseract boxes | no (approx) |
| 19 | Face blur | Auto-detect and blur faces | Cloudinary AI, Brighter AI | 30 | opencv YuNet | no (approx) |
| 20 | Image diff | Pixel and perceptual diff of two images | Percy, Applitools | 199 | odiff, pixelmatch, imagemagick compare | no (approx) |
| 21 | Contact sheet | Grid montage of many images with labels | Adobe Bridge, Lightroom | 10 | imagemagick montage | no (approx) |
| 22 | Sprite sheet packer | Pack images into one atlas plus JSON map | TexturePacker | 5 | pillow, rectpack | no (approx) |
| 23 | Auto-orient image | Rotate by EXIF orientation and clear the tag | none/glue | 0 | exiftool, pillow ImageOps | no (approx) |
| 24 | Rounded corners/border/shadow | Decorate an image for docs or listings | Canva, Shots.so | 10 | pillow | no (approx) |
| 25 | PNG to ICO/ICNS | Build Windows .ico or macOS .icns | IconWorkshop | 0 | imagemagick, png2icns | no (approx) |
| 26 | Open Graph card | Render social preview image from title and template | Bannerbear, Placid | 49 | pillow, satori, headless chromium | no (approx) |
| 27 | Placeholder image | Generate sized placeholder with text | placehold.co (free tier) | 0 | pillow | no (approx) |
| 28 | Image OCR | Extract text from an image with boxes | Adobe Acrobat OCR, ABBYY | 20 | tesseract | no (approx) |
| 29 | QR code generate | Make QR as PNG or SVG with logo option | QR Code Generator Pro | 7 | qrencode, segno | no (approx) |
| 30 | QR/barcode read | Decode QR and barcodes from an image | Scanbot SDK | 20 | zbar, pyzbar | no (approx) |
| 31 | Duplicate image finder | Find near-duplicate photos by perceptual hash | PhotoSweeper | 10 | imagehash, pillow | no (approx) |
| 32 | Image to base64 | Encode an image as a data URI | none/glue | 0 | python stdlib | no (approx) |
| 33 | URL screenshot | Full page PNG of a URL at set viewport | Urlbox, ScreenshotOne | 19 | playwright, headless chromium | no (approx) |
| 34 | Images to PDF | Combine images into one PDF | Smallpdf, iLovePDF | 9 | img2pdf, imagemagick | no (approx) |
| 35 | Caption or text overlay | Add caption or meme text on an image | Kapwing, Canva | 16 | pillow | no (approx) |
| 36 | Compress PDF | Reduce PDF size by quality preset | iLovePDF, Smallpdf | 9 | ghostscript, qpdf | no (approx) |
| 37 | Merge PDFs | Join several PDFs in order | Smallpdf, Acrobat | 12 | qpdf, pypdf | no (approx) |
| 38 | Split PDF | Split into single pages or chunks | Smallpdf | 12 | qpdf | no (approx) |
| 39 | Extract PDF page range | Pull chosen pages into a new PDF | Acrobat Pro | 20 | qpdf | no (approx) |
| 40 | Rotate PDF pages | Rotate chosen pages 90 or 180 | Smallpdf | 12 | qpdf, pypdf | no (approx) |
| 41 | PDF to images | Render pages to PNG or JPG | CloudConvert, Zamzar | 9 | pdftoppm (poppler), pymupdf | no (approx) |
| 42 | PDF text extract | Get text with layout, page by page | Adobe Export | 20 | pdftotext, pymupdf | no (approx) |
| 43 | OCR a scanned PDF | Add a searchable text layer | Acrobat Pro, ABBYY FineReader | 20 | ocrmypdf (tesseract) | no (approx) |
| 44 | Markdown to PDF | Render markdown with a stylesheet to PDF | Typora, Notion export | 10 | pandoc, weasyprint | no (approx) |
| 45 | HTML to PDF | Print HTML or URL to PDF | PDFShift, Api2Pdf | 9 | weasyprint, headless chromium | no (approx) |
| 46 | DOCX to PDF | Convert Word docs to PDF | Smallpdf, Adobe | 12 | libreoffice headless | no (approx) |
| 47 | PDF to DOCX | Convert PDF into editable Word | Acrobat Pro, Smallpdf | 20 | pdf2docx, libreoffice | no (approx) |
| 48 | Extract images from docx/pptx/xlsx | Pull embedded media from Office files | none/glue | 0 | unzip on the OOXML package | no (approx) |
| 49 | DOCX to Markdown | Convert Word to clean markdown with images | none/glue | 0 | pandoc | no (approx) |
| 50 | Markdown to DOCX | Markdown to styled Word doc with reference template | Typora | 10 | pandoc reference.docx | no (approx) |
| 51 | PDF password add/remove | Encrypt or unlock PDF (given password) | Acrobat Pro | 20 | qpdf | no (approx) |
| 52 | PDF metadata edit/strip | Read, set or clear title, author, XMP | Acrobat Pro | 20 | exiftool, qpdf | no (approx) |
| 53 | PDF watermark or stamp | Overlay text or image on every page | Acrobat Pro, PDFescape | 20 | pypdf, reportlab | no (approx) |
| 54 | PDF page numbers | Add page numbers or Bates stamps | Acrobat Pro | 20 | pypdf, reportlab | no (approx) |
| 55 | PDF table extract | Pull tables from PDF into CSV | Docparser, Nanonets | 32 | camelot, pdfplumber | no (approx) |
| 56 | Fill PDF form | Fill AcroForm fields from JSON | pdfFiller, Jotform PDF | 8 | pypdf, pdftk | no (approx) |
| 57 | Flatten or linearize PDF | Flatten forms and annotations, fast web view | Acrobat Pro | 20 | qpdf, ghostscript | no (approx) |
| 58 | Sign PDF | Place signature image or digital cert signature | DocuSign, Dropbox Sign | 10 | pyHanko, pypdf | no (approx) |
| 59 | PDF to PDF/A | Convert for archival compliance | Acrobat Pro | 20 | ghostscript | no (approx) |
| 60 | PDF redaction | Permanently remove matched text and areas | Acrobat Pro | 20 | pymupdf redactions | no (approx) |
| 61 | PDF bookmarks and TOC | Read or set outline entries | Acrobat Pro | 20 | pypdf | no (approx) |
| 62 | Compare two PDFs | Visual and text diff of two PDFs | Draftable | 15 | diff-pdf, pymupdf, difflib | no (approx) |
| 63 | Markdown to EPUB | Build an ebook from markdown chapters | Vellum, Atticus | 15 | pandoc | no (approx) |
| 64 | Ebook convert | EPUB, MOBI, AZW3, PDF conversion | Calibre (free), Zamzar | 9 | calibre ebook-convert | no (approx) |
| 65 | CSV/XLSX convert | CSV, XLSX, ODS, JSON table conversion | CloudConvert | 9 | pandas, libreoffice | no (approx) |
| 66 | PPTX to PDF or images | Export slides to PDF or PNG per slide | Smallpdf, Zamzar | 12 | libreoffice headless, pdftoppm | no (approx) |
| 67 | Text diff of documents | Compare two docx or text files with changes marked | Draftable, Word Compare | 15 | pandoc, difflib | no (approx) |
| 68 | Word count and readability | Words, reading time, grade level for a doc | Hemingway Editor | 0 | pandoc, textstat | no (approx) |
| 69 | Extract audio from video | Pull the audio track to mp3, wav, m4a | Zamzar, Kapwing | 16 | ffmpeg | no (approx) |
| 70 | Audio format convert | Convert between mp3, wav, flac, ogg, opus, m4a | CloudConvert, Zamzar | 9 | ffmpeg | no (approx) |
| 71 | Trim silence | Cut leading, trailing and long gap silence | Descript, Auphonic | 24 | ffmpeg silenceremove | no (approx) |
| 72 | Loudness normalize | Normalize to LUFS target (podcast -16) | Auphonic | 11 | ffmpeg loudnorm two-pass | no (approx) |
| 73 | Speech to text | Transcribe audio or video with timestamps | Otter.ai, Rev | 17 | faster-whisper | no (approx) |
| 74 | Transcript to SRT/VTT | Make subtitle files from audio | Rev, Descript | 24 | faster-whisper, srt writer | no (approx) |
| 75 | Text to speech | Read text aloud to wav or mp3 | ElevenLabs, Play.ht | 22 | piper, kokoro | no (approx) |
| 76 | Audio trim or cut | Cut a segment by timestamps | Clideo | 9 | ffmpeg -ss -to | no (approx) |
| 77 | Audio concat | Join clips with optional crossfade | Clideo | 9 | ffmpeg concat, acrossfade | no (approx) |
| 78 | Noise reduction | Denoise speech recordings | Adobe Podcast Enhance, Krisp | 10 | rnnoise, DeepFilterNet | no (approx) |
| 79 | Audio tags read/write | Edit ID3, cover art and tags | Mp3tag (free), Kid3 | 0 | mutagen | no (approx) |
| 80 | Audio waveform image | Render waveform PNG or waveform video | Headliner, Wavve | 20 | ffmpeg showwavespic, audiowaveform | no (approx) |
| 81 | BPM and key detect | Estimate tempo and musical key | Mixed In Key | 4 | librosa, essentia | no (approx) |
| 82 | Stem separation | Split vocals, drums, bass, other | LALAL.AI, Moises | 15 | demucs | no (approx) |
| 83 | Audio speed or pitch | Change tempo without pitch shift, or pitch alone | Clideo | 9 | ffmpeg atempo, rubberband | no (approx) |
| 84 | Media probe | Duration, codecs, bitrate, resolution, streams for any media | none/glue | 0 | ffprobe | no (approx) |
| 85 | Video frame or thumbnail | Grab a frame at a timestamp or N evenly spaced | Kapwing, Clideo | 16 | ffmpeg | no (approx) |
| 86 | Video compress | Shrink video to target size or CRF | Clideo, VEED | 9 | ffmpeg x264/x265 | no (approx) |
| 87 | Video trim lossless | Cut a range without re-encoding | Clideo, Kapwing | 16 | ffmpeg -c copy | no (approx) |
| 88 | Video concat | Join clips, re-encode if formats differ | Kapwing, Clipchamp | 16 | ffmpeg concat | no (approx) |
| 89 | Burn in subtitles | Hardcode SRT or VTT with style | Kapwing, VEED | 18 | ffmpeg subtitles filter | no (approx) |
| 90 | Video resize or reframe | Crop or pad to 9:16, 1:1, 16:9 | Kapwing, Opus Clip | 16 | ffmpeg crop, pad, scale | no (approx) |
| 91 | Video speed change | Speed up or slow down with audio kept in sync | Kapwing | 16 | ffmpeg setpts, atempo | no (approx) |
| 92 | Video watermark | Overlay logo with position and opacity | VEED, Kapwing | 18 | ffmpeg overlay | no (approx) |
| 93 | Scene detection | List scene cuts and split by scene | Frame.io | 15 | PySceneDetect | no (approx) |
| 94 | Video stabilize | Reduce camera shake | Adobe Premiere | 23 | ffmpeg vidstab | no (approx) |
| 95 | Video storyboard | Tile frames into a contact sheet from a video | Frame.io | 15 | ffmpeg tile filter | no (approx) |
| 96 | Replace or remove audio track | Mute or swap the audio on a video | Clideo, Kapwing | 16 | ffmpeg -map | no (approx) |
| 97 | Archive extract or create | Zip, tar, 7z, rar (read) with path traversal guard | WinZip, WinRAR | 3 | libarchive, 7z | no (approx) |
| 98 | File type detect | Real type by magic bytes, not extension | none/glue | 0 | libmagic | no (approx) |
| 99 | Checksum and verify | SHA-256, MD5 hash of files and verify against a list | none/glue | 0 | coreutils, python hashlib | no (approx) |
| 100 | Batch rename | Rename by pattern, EXIF date, or counter | Advanced Renamer | 0 | exiftool, python pathlib | no (approx) |

## Top 12 must-haves (ranked)

1. Media probe (ffprobe metadata and duration), every agent needs it first
2. Extract audio from video
3. Speech to text (Whisper) plus transcript to SRT/VTT
4. Compress PDF
5. Merge PDFs and split PDF
6. Strip image metadata (EXIF and GPS)
7. HEIC to JPG/PNG
8. Markdown to PDF and DOCX to PDF
9. OCR a scanned PDF
10. Compress images and convert to WebP/AVIF
11. Remove background
12. Video compress and video trim lossless

## Near-dupes merged

- Merge PDFs, Split PDF and Extract PDF page range can ship as one pdf-pages tool with three modes.
- Extract audio from video and Audio format convert can share one ffmpeg audio tool.
- Speech to text and Transcript to SRT/VTT are one Whisper job with two output formats.
- Video clip to GIF, GIF from frames and GIF to MP4 share one ffmpeg animation tool.
- Read image metadata and Media probe can share one metadata tool with an image path and a media path.
- Markdown to PDF, HTML to PDF and URL screenshot share the headless renderer.
