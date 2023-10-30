package com.example.mycatalog;

// Import necessary Android classes
import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;


// Define CatalogActivity class that extends AppCompatActivity
public class CatalogActivity extends AppCompatActivity {
    private Button toDetailButton;
    // Declare a Context object and initialize it to the current instance of this class
    private Context context = this;
    // Override the onCreate method that is called when the activity is first created
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        // Call the superclass's onCreate method and pass in the saved state of the application
        super.onCreate(savedInstanceState);
        // Set the layout for this activity as activity_main
        setContentView(R.layout.activity_main);
        // Locate the button in our layout by its ID and assign it to our toDetailButton member variable
        toDetailButton = findViewById(R.id.button_to_detail);
        // Set an OnClickListener for the button
        toDetailButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // When the button is clicked, create an Intent to start DetailActivity
                Intent intent = new Intent(context, DetailActivity.class);
                // Start an instance of DetailActivity
                startActivity(intent);
            }
        });
    }
}