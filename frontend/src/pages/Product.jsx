import Header from "../components/Header";
import Footer from "../components/Footer";

function Product() {
  return (
    <>
      <Header />

      <main
        style={{
          maxWidth: 1000,
          margin: "40px auto",
          padding: 20,
        }}
      >
        <h2>Product Details</h2>

        <p>
          This page will display:
        </p>

        <ul>
          <li>Product information</li>
          <li>AI summary</li>
          <li>Pros & Cons</li>
          <li>Comparison</li>
          <li>Buy button</li>
        </ul>
      </main>

      <Footer />
    </>
  );
}

export default Product;