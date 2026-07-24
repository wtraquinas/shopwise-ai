import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";

import api from "../services/api";

import Header from "../components/Header";
import Footer from "../components/Footer";
import Loading from "../components/Loading";
import ProductCard from "../components/ProductCard";

function Category() {
  const { id } = useParams();

  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api
      .get(`/api/products?category=${id}`)
      .then((response) => {
        setProducts(response.data.data || response.data);
      })
      .catch(console.error)
      .finally(() => setLoading(false));
  }, [id]);

  return (
    <>
      <Header />

      <main
        style={{
          maxWidth: 1200,
          margin: "40px auto",
          padding: 20,
        }}
      >
        <h2>{id}</h2>

        {loading ? (
          <Loading />
        ) : (
          <div
            style={{
              display: "grid",
              gap: 20,
              gridTemplateColumns:
                "repeat(auto-fit,minmax(250px,1fr))",
              marginTop: 30,
            }}
          >
            {products.map((product) => (
              <ProductCard
                key={product.id}
                product={product}
              />
            ))}
          </div>
        )}
      </main>

      <Footer />
    </>
  );
}

export default Category;