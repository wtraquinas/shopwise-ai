const API = import.meta.env.VITE_API_URL;

export async function getProducts(category = "") {
  const url = category
    ? `${API}/api/products?category=${category}`
    : `${API}/api/products`;

  const response = await fetch(url);

  if (!response.ok) {
    throw new Error("Unable to load products");
  }

  const json = await response.json();

  return json.data;
}

export async function getProduct(id) {
  const response = await fetch(`${API}/api/products/${id}`);

  const json = await response.json();

  return json.data;
}