import os

def scan_reviews(reviews_root='reviews'):
    """
    Walk through the reviews directory, grouping review files by city.
    Reviews placed directly under reviews/ are put under an 'Uncategorized' category.
    """
    reviews_by_city = {}
    for root, dirs, files in os.walk(reviews_root):
        for file in files:
            if file.endswith('.html'):
                # Determine the city folder by computing the relative directory
                rel_dir = os.path.relpath(root, reviews_root)
                city = rel_dir if rel_dir != '.' else 'Uncategorized'
                reviews_by_city.setdefault(city, []).append(file)
    return reviews_by_city

def generate_index_html(reviews_by_city):
    """
    Build an index.html file using the grouped reviews.
    """
    # Header part of the index page
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Denmark Kebab & Shawarma Blog</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header>
    <div class="container">
      <h1>Denmark Kebab & Shawarma Blog</h1>
      <nav>
        <ul>
          <li><a href="#reviews">Reviews</a></li>
        </ul>
      </nav>
    </div>
  </header>
  <main class="container">
    <section id="reviews">
      <h2>Latest Reviews</h2>
'''

    # Loop over each city category and its review files
    for city, files in reviews_by_city.items():
        # Use the folder name as the city title (with proper capitalization)
        city_title = city if city != 'Uncategorized' else 'Diverse'
        html_content += f'      <section id="{city}">\n'
        html_content += f'        <h3>{city_title.title()}</h3>\n'
        html_content += '        <div class="reviews">\n'
        for file in sorted(files):
            # If reviews are organized in subdirectories, build the file path accordingly:
            file_path = os.path.join('reviews', city, file) if city != 'Uncategorized' else os.path.join('reviews', file)
            # Create a title from the file name (remove extension, replace hyphens/underscores with spaces)
            title = os.path.splitext(file)[0].replace('-', ' ').replace('_', ' ').title()
            html_content += '          <article class="review">\n'
            html_content += f'            <h4>{title}</h4>\n'
            html_content += f'            <a class="read-more" href="{file_path}">Read Full Review</a>\n'
            html_content += '          </article>\n'
        html_content += '        </div>\n'
        html_content += '      </section>\n'

    # Append a Fun Fact box and footer
    html_content += '''    </section>
    <aside class="fact-box">
      <h3>Fun Kebab & Shawarma Facts!</h3>
      <div id="fact-content">
        <p id="fact-text">Did you know that shawarma originally comes from the Middle East and means "turning"? The meat is cooked on a rotating spit!</p>
      </div>
      <button id="next-fact">Next Fact</button>
    </aside>
  </main>
  <footer>
    <p>&copy; 2025 Denmark Kebab & Shawarma Blog</p>
  </footer>
  <script src="scripts.js"></script>
</body>
</html>
'''
    return html_content

if __name__ == '__main__':
    # Scan the reviews directory for review files
    reviews_by_city = scan_reviews()
    # Generate the index.html content
    index_html = generate_index_html(reviews_by_city)
    # Write the generated content to index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(index_html)
    print("index.html has been generated successfully.")

