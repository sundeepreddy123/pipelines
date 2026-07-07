import { Link } from "react-router-dom";


function Navbar(){

return(

<nav>

<h2>
Sundeep Store
</h2>


<Link to="/">
Home
</Link>


{" | "}


<Link to="/products">
Products
</Link>


</nav>

);

}


export default Navbar;