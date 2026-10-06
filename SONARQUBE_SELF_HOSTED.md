# SonarQube Self-Hosted Setup for this Repository

This repo's Sonar scan is configured to analyze the `product-service` Maven module.

## What code is scanned

The GitHub Actions workflow step uses:

```yaml
- name: SonarQube Scan
  if: ${{ secrets.SONAR_TOKEN != '' && secrets.SONAR_HOST_URL != '' }}
  working-directory: product-service
  uses: SonarSource/sonarqube-scan-action@v8.2.1
  env:
    SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
    SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}
```

That means the scanner runs from the `product-service` folder and analyzes the Java project defined by `product-service/pom.xml`.

## Repository / project mapping in SonarQube

SonarQube identifies the project using a project key.
In this repo, the Maven project is:

- `groupId`: `com.ecommerce`
- `artifactId`: `product-service`
- `version`: `1.0.0`

A good Sonar project key is:

```text
com.ecommerce:product-service
```

If you do not provide an explicit `sonar.projectKey`, the Maven scanner will usually infer the project key from the POM coordinates.

## How to configure SonarQube self-hosted

1. Run SonarQube locally or on a server.

   Quick test:
   ```bash
   docker run -d --name sonarqube -p 9000:9000 sonarqube:lts
   ```

   Better for stable use:
   ```yaml
   version: '3.7'
   services:
     db:
       image: postgres:13
       environment:
         POSTGRES_USER: sonar
         POSTGRES_PASSWORD: sonar
         POSTGRES_DB: sonarqube
       volumes:
         - sonar-db:/var/lib/postgresql/data
     sonarqube:
       image: sonarqube:lts
       depends_on:
         - db
       environment:
         SONAR_JDBC_URL: jdbc:postgresql://db:5432/sonarqube
         SONAR_JDBC_USERNAME: sonar
         SONAR_JDBC_PASSWORD: sonar
       ports:
         - "9000:9000"
       ulimits:
         nofile:
           soft: 65536
           hard: 65536
   volumes:
     sonar-db:
   ```

2. Open SonarQube at `http://localhost:9000` and sign in.
3. Create a new project in SonarQube with a key like `com.ecommerce:product-service`.
4. Generate an analysis token in SonarQube: `My Account` → `Security` → `Generate Tokens`.
5. Add GitHub repository secrets:
   - `SONAR_TOKEN` = the token
   - `SONAR_HOST_URL` = your SonarQube URL, for example `http://your-server:9000`

## GitHub Actions and reachability

- If you use GitHub-hosted runners, SonarQube must be reachable from the public internet.
- If SonarQube is private, use a self-hosted GitHub Actions runner on the same network.

## If you are not sure which repo Sonar scans

This workflow scans `product-service` only, not the entire repository root.
So the Sonar project should be linked to the Java service in `product-service`.

## Optional explicit project key

If you want to force the key, you can add `sonar.projectKey` to the Maven command or Sonar config.
For example:

```yaml
run: mvn clean test sonar:sonar -Dsonar.projectKey=com.ecommerce:product-service -Dsonar.host.url=${{ secrets.SONAR_HOST_URL }} -Dsonar.login=${{ secrets.SONAR_TOKEN }}
```

This repo does not currently include a dedicated `sonar-project.properties` file, so the safest path is to use the Maven module and the project key above.
