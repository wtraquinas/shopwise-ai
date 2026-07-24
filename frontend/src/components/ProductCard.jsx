function ProductCard({ product }) {
  return (
    <div
      style={{
        border: "1px solid #ddd",
        borderRadius: 10,
        padding: 20,
        background: "white",
      }}
    >
      <img
        src={product.image}
        alt={product.title}
        style={{
          width: "100%",
          maxHeight: 220,
          objectFit: "contain",
        }}
      />

      <h3
        style={{
          marginTop: 15,
        }}
      >
        {product.title}
      </h3>

      <p>{product.brand}</p>

      <p>
        ⭐ {product.rating}
      </p>

      <h2>
        {product.currency} {product.price}
      </h2>

      <button
        style={{
          marginTop: 15,
          padding: "10px 20px",
        }}
      >
        View Details
      </button>
    </div>
  );
}

export default ProductCard;