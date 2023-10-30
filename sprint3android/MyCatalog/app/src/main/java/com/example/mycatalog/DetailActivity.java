package com.example.mycatalog;
// Import necessary Android classes
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
// Define DetailActivity class that extends AppCompatActivity
public class DetailActivity extends AppCompatActivity {
    // Override the onCreate method that is called when the activity is first created
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        // Call the superclass's onCreate method and pass in the saved state of the application
        super.onCreate(savedInstanceState);
        // Set the layout for this activity as activity_detail
        setContentView(R.layout.activity_detail);
    }
}