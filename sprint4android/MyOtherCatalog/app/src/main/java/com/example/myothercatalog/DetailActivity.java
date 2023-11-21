package com.example.myothercatalog;

import android.content.Intent;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class DetailActivity extends AppCompatActivity {
    // TextView to display the emperor's name
    private TextView textView;
    // ImageView to display the emperor's image
    private ImageView imageView;
    // TextView to display the emperor's description
    private TextView descriptionTextView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        // Call the superclass's onCreate method and pass in the saved state of the application
        super.onCreate(savedInstanceState);
        // Set the layout for this activity as activity_detail
        setContentView(R.layout.activity_detail);
        // Get the intent along with its extras
        Intent intent = getIntent();
        String name = intent.getStringExtra("name");
        String description = intent.getStringExtra("description");
        String url = intent.getStringExtra("url");
        textView = findViewById(R.id.name);
        imageView = findViewById(R.id.pic);
        descriptionTextView = findViewById(R.id.description);
        // Add the extras to the layout
        textView.setText(name);
        Util.downloadBitmapToImageView(url, this.imageView);
        descriptionTextView.setText(description);
    }
}
