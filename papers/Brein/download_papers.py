import os
import urllib.request
import urllib.error
import time

PAPERS = [
    {
        "filename": "1982_Hopfield_PNAS.pdf",
        "title": "Neural networks and physical systems with emergent computational abilities",
        "authors": "J. J. Hopfield (1982)",
        "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC346238/pdf/pnas00641-0304.pdf",
        "type": "Open Access (PNAS / PMC)",
    },
    {
        "filename": "2009_Burak_Fiete_PLoSCompBiol.pdf",
        "title": "Accurate path integration in continuous attractor network models of grid cells",
        "authors": "Y. Burak, I. R. Fiete (2009)",
        "url": "https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1000291&type=printable",
        "type": "Open Access (PLoS)",
    },
    {
        "filename": "2016_Benna_Fusi_arXiv.pdf",
        "title": "Computational principles of biological memory",
        "authors": "M. K. Benna, S. Fusi (2016)",
        "url": "https://arxiv.org/pdf/1507.07580.pdf",
        "type": "Open Access Preprint (arXiv:1507.07580)",
    },
    {
        "filename": "2016_Krotov_Hopfield_Dense_Associative_Memory.pdf",
        "title": "Dense Associative Memory for Pattern Recognition",
        "authors": "D. Krotov, J. J. Hopfield (2016)",
        "url": "https://arxiv.org/pdf/1606.01164.pdf",
        "type": "Open Access Preprint (arXiv:1606.01164)",
    },
    {
        "filename": "2020_Ramsauer_Hopfield_Networks_All_You_Need.pdf",
        "title": "Hopfield Networks is All You Need",
        "authors": "H. Ramsauer et al. (2020)",
        "url": "https://arxiv.org/pdf/2008.02217.pdf",
        "type": "Open Access Preprint (arXiv:2008.02217)",
    },
    {
        "filename": "2022_Khona_Fiete_Attractor_Networks.pdf",
        "title": "Attractor and integrator networks in the brain",
        "authors": "M. Khona, I. R. Fiete (2022)",
        "url": "https://arxiv.org/pdf/2112.03978.pdf",
        "type": "Open Access Preprint (arXiv:2112.03978)",
    },
]

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

output_dir = os.path.dirname(os.path.abspath(__file__))

print(f"Downloading {len(PAPERS)} open-access papers to: {output_dir}")

for item in PAPERS:
    filepath = os.path.join(output_dir, item["filename"])
    print(f"\nFetching: {item['title']} ({item['authors']})...")
    req = urllib.request.Request(item["url"], headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            content = response.read()
            if len(content) < 1000 or not content.startswith(b"%PDF"):
                print(
                    f"Warning: downloaded file does not appear to be a valid PDF (size: {len(content)} bytes). Response preview: {content[:100]}"
                )
            else:
                with open(filepath, "wb") as f:
                    f.write(content)
                print(
                    f"Successfully saved to {item['filename']} ({len(content) / (1024 * 1024):.2f} MB)"
                )
        time.sleep(1)  # respectful delay
    except Exception as e:
        print(f"Failed to download from {item['url']}: {e}")

print("\nDone!")
