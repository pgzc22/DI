package com.example.myothercatalog;

import android.app.Activity;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

public class EmperorViewHolder extends RecyclerView.ViewHolder {
    private final TextView textView;
    private final ImageView imageView;
    public EmperorViewHolder(@NonNull View itemView){
        super (itemView);
        textView = (TextView) itemView.findViewById(R.id.emperor_text_view);
        imageView = (ImageView) itemView.findViewById(R.id.emperor_image_view);
    }
    public void showData(EmperorData data, Activity activity){
        textView.setText(data.getName());
        Util.downloadBitmapToImageView(data.getImageUrl(), this.imageView);
    }
}
