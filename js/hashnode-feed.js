const HASHNODE_USERNAME = 'aryanmdev';
const HASHNODE_API = 'https://gql.hashnode.com/';

export async function fetchHashnodePosts() {
  const query = `
    query {
      user(username: "${HASHNODE_USERNAME}") {
        publications(first: 1) {
          edges {
            node {
              posts(first: 3) {
                edges {
                  node {
                    title
                    brief
                    slug
                    publishedAt
                    readTimeInMinutes
                    coverImage { url }
                  }
                }
              }
            }
          }
        }
      }
    }
  `;

  try {
    const res  = await fetch(HASHNODE_API, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query })
    });
    const json = await res.json();
    const posts = json.data?.user?.publications?.edges?.[0]?.node?.posts?.edges || [];
    renderPosts(posts.map(e => e.node));
  } catch {
    document.getElementById('blog-container').innerHTML =
      '<p class="muted">Could not load posts. <a href="https://aryanmdev.hashnode.dev" target="_blank">Read on Hashnode ↗</a></p>';
  }
}

function renderPosts(posts) {
  const container = document.getElementById('blog-container');
  container.innerHTML = posts.map(post => `
    <a class="blog-card" href="https://aryanmdev.hashnode.dev/${post.slug}" target="_blank" rel="noopener">
      <div class="blog-meta">
        <span class="blog-date">${new Date(post.publishedAt).toLocaleDateString('en-IN', { month:'short', year:'numeric' })}</span>
        <span class="blog-read">${post.readTimeInMinutes} min read</span>
      </div>
      <h3 class="blog-title">${post.title}</h3>
      <p class="blog-brief">${post.brief}</p>
      <span class="blog-cta">Read article →</span>
    </a>
  `).join('');
}


