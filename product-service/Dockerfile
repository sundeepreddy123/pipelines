# Use Java 21 Runtime
FROM eclipse-temurin:21-jre

# Application directory
WORKDIR /app

# Copy the Spring Boot JAR
COPY target/product-service-1.0.0.jar app.jar

# Application Port
EXPOSE 8080

# Start Application
ENTRYPOINT ["java","-jar","app.jar"]