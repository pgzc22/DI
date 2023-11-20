package com.example.myothercatalog;

import android.app.Activity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class EmperorRecyclerViewAdapter extends RecyclerView.Adapter<EmperorViewHolder> {
    private List<EmperorData> allTheData;
    private Activity activity;
    public EmperorRecyclerViewAdapter(List<EmperorData> dataSet, Activity activity) {
        this.allTheData = dataSet;
        this.activity = activity;
    }

    @NonNull
    @Override
    public EmperorViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.emperor_recycler_cell, parent, false);
        return new EmperorViewHolder(view);
    }

    public void onBindViewHolder(EmperorViewHolder holder, int position){
        EmperorData dataInPositionToBeRendered = allTheData.get(position);
        holder.showData(dataInPositionToBeRendered, activity);
    }
    public int getItemCount(){
        return allTheData.size();
    }
}
