package com.example.myothercatalog;

// Importing necessary libraries
import static androidx.core.content.ContextCompat.startActivity;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

// ViewHolder class for the RecyclerView
public class EmperorViewHolder extends RecyclerView.ViewHolder {
    // TextView to display the emperor's name
    private final TextView textView;
    // ImageView to display the emperor's image
    private final ImageView imageView;
    // Button to switch to DetailActivity
    private final Button button;
    // Constructor for the ViewHolder
    public EmperorViewHolder(@NonNull View itemView){
        super (itemView);
        // Initializing the TextView and ImageView
        textView = (TextView) itemView.findViewById(R.id.emperor_text_view);
        imageView = (ImageView) itemView.findViewById(R.id.emperor_image_view);
        button = (Button) itemView.findViewById(R.id.button);
    }
    // Method to display the data in the ViewHolder
    public void showData(EmperorData data, Activity activity){
        // Setting the text of the TextView to the emperor's name
        textView.setText(data.getName());
        // Downloading the image from the URL and setting it to the ImageView
        Util.downloadBitmapToImageView(data.getImageUrl(), this.imageView);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Context context = v.getContext();
                Intent intent = new Intent(context, DetailActivity.class);
                intent.putExtra("name", data.getName());
                intent.putExtra("description", data.getDescription());
                intent.putExtra("url", data.getImageUrl());
                context.startActivity(intent);
            }
        });
    }
}
