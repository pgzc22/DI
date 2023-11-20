package com.example.myothercatalog;

// Importing necessary libraries
import android.app.Activity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

// Adapter class for the RecyclerView
public class EmperorRecyclerViewAdapter extends RecyclerView.Adapter<EmperorViewHolder> {
    // List of EmperorData objects
    private List<EmperorData> allTheData;
    // Activity where the RecyclerView is located
    private Activity activity;
    // Constructor for the adapter
    public EmperorRecyclerViewAdapter(List<EmperorData> dataSet, Activity activity) {
        this.allTheData = dataSet;
        this.activity = activity;
    }

    @NonNull
    @Override
    // Method to create a new ViewHolder
    public EmperorViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        // Inflating the layout for each item of the RecyclerView
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.emperor_recycler_cell, parent, false);
        // Returning a new ViewHolder
        return new EmperorViewHolder(view);
    }

    // Method to bind data to the ViewHolder
    public void onBindViewHolder(EmperorViewHolder holder, int position){
        // Getting the EmperorData object at the current position
        EmperorData dataInPositionToBeRendered = allTheData.get(position);
        // Displaying the data in the ViewHolder
        holder.showData(dataInPositionToBeRendered, activity);
    }
    // Method to get the number of items in the data set
    public int getItemCount(){
        return allTheData.size();
    }
}
