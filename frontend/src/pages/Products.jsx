import {useEffect,useState} from "react";
import ProductCard from "../components/ProductCard";
import {getProducts} from "../services/productService";


function Products(){


const [products,setProducts]=useState([]);



useEffect(()=>{

    getProducts()
    .then(data=>{

        console.log("Products from API:", data);

        setProducts(data);

    })
    .catch(error => {
        console.log("Error fetching products:", error);
    });

},[]);


return(

<div>

<h1>
Products
</h1>


{
products.map(product=>(

<ProductCard
key={product.id}
product={product}
/>

))
}


</div>


);


}


export default Products;