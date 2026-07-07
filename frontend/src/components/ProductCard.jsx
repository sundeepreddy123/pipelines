import { Link } from "react-router-dom";


function ProductCard({product}){


return(

<div className="productcard">


<img
src={`http://localhost:8081${product.image}`}
alt={product.name}
width="200"
/>


<h3>
{product.name}
</h3>


<p>
Category: {product.category}
</p>


<p>
Price: ₹{product.price}
</p>


<Link 
to={`/products/${product.id}`}
>
View Details
</Link>


</div>


);


}


export default ProductCard;