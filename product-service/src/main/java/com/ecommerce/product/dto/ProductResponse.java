package com.ecommerce.product.dto;

public class ProductResponse {

    private Long id;
    private String name;
    private String description;
    private Double price;
    private String image;

    public ProductResponse() {
    }

    public ProductResponse(Long id, String name, String description, Double price, String image) {
        this.id = id;
        this.name = name;
        this.description = description;
        this.price = price;
        this.image = image;
    }

    public Long getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getDescription() {
        return description;
    }

    public Double getPrice() {
        return price;
    }

    public String getImage() {
        return image;
    }
}