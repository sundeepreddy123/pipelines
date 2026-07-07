package com.ecommerce.product.service;

import com.ecommerce.product.dto.ProductResponse;
import com.ecommerce.product.dto.ProductRequest;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class ProductServiceImpl implements ProductService {

    private final List<ProductResponse> products = new ArrayList<>();

    public ProductServiceImpl() {

        products.add(new ProductResponse(
                1L,
                "iPhone 16",
                "Apple iPhone 16 256GB",
                1200.0,
                "/images/iphone16.jpg"
        ));

        products.add(new ProductResponse(
                2L,
                "Samsung Galaxy S25",
                "Samsung Galaxy S25 256GB",
                1100.0,
                "/images/samsung-s25.jpg"
        ));

        products.add(new ProductResponse(
                3L,
                "MacBook Pro",
                "Apple MacBook Pro M4",
                2200.0,
                "/images/macbook-pro.jpg"
        ));

        products.add(new ProductResponse(
                4L,
                "Apple Watch",
                "Series 10",
                499.0,
                "/images/apple-watch.jpg"
        ));

        products.add(new ProductResponse(
                5L,
                "AirPods Pro",
                "Apple AirPods Pro 2",
                249.0,
                "/images/airpods-pro.jpg"
        ));

        products.add(new ProductResponse(
                6L,
                "PS5 Controller",
                "Sony DualSense Controller",
                79.0,
                "/images/ps5-controller.jpg"
        ));
    }

    @Override
    public List<ProductResponse> getAllProducts() {
        return products;
    }

    @Override
    public ProductResponse getProduct(Long id) {

        return products.stream()
                .filter(product -> product.getId().equals(id))
                .findFirst()
                .orElse(null);
    }

    @Override
    public ProductResponse addProduct(ProductRequest request) {

        Long id = (long) (products.size() + 1);

        ProductResponse product = new ProductResponse(
                id,
                request.getName(),
                request.getDescription(),
                request.getPrice(),
                request.getImage()
        );

        products.add(product);

        return product;
    }

    @Override
    public ProductResponse updateProduct(Long id, ProductRequest request) {

        for (int i = 0; i < products.size(); i++) {

            ProductResponse product = products.get(i);

            if (product.getId().equals(id)) {

                ProductResponse updated = new ProductResponse(
                        id,
                        request.getName(),
                        request.getDescription(),
                        request.getPrice(),
                        request.getImage()
                );

                products.set(i, updated);

                return updated;
            }
        }

        return null;
    }

    @Override
    public void deleteProduct(Long id) {

        products.removeIf(product -> product.getId().equals(id));
    }
        
}
