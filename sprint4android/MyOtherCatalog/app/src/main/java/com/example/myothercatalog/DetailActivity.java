package com.example.myothercatalog;

import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;

public class DetailActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        // Call the superclass's onCreate method and pass in the saved state of the application
        super.onCreate(savedInstanceState);
        // Set the layout for this activity as activity_detail
        setContentView(R.layout.activity_detail);
    }
}
