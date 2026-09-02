package com.example.demo.application;

import com.example.demo.domain.Product;
import com.example.demo.infrastructure.ProductRepository;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.when;

@ExtendWith(MockitoExtension.class)
class ProductServiceTest {

    @Mock
    private ProductRepository productRepository;

    @InjectMocks
    private ProductService productService;

    @Test
    void shouldReturnAllProducts() {
        // Preparar (Arrange)
        Product mockProduct = new Product("Café Latte", 3500.0);
        when(productRepository.findAll()).thenReturn(List.of(mockProduct));

        // Ejecutar (Act)
        List<Product> result = productService.getAllProducts();

        // Validar (Assert)
        assertEquals(1, result.size());
        assertEquals("Café Latte", result.get(0).getName());
    }
}