import axios from "axios";


const API_URL = "http://localhost:8080/api";


export const getProducts = async () => {

    const response = await axios.get(
        `${API_URL}/products`
    );

    return response.data;

};