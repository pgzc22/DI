package com.example.mycatalog.ui.catalog;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;

import com.example.mycatalog.DetailActivity;
import com.example.mycatalog.R;
import com.example.mycatalog.databinding.FragmentCatalogBinding;
import com.example.mycatalog.ui.detail.DetailFragment;

public class CatalogFragment extends Fragment {

    private FragmentCatalogBinding binding;
    private Button toDetailButton;

    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {

        // Inflate the layout for this fragment using FragmentCatalogBinding
        binding = FragmentCatalogBinding.inflate(inflater, container, false);
        View root = binding.getRoot();

        toDetailButton = root.findViewById(R.id.button_to_detail);
        // Set an OnClickListener for the button
        toDetailButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // When the button is clicked, create an Intent to start DetailActivity
                Intent intent = new Intent(getActivity(), DetailActivity.class);
                // Start an instance of DetailActivity
                startActivity(intent);
            }
        });
        // Return the root view
        return root;
    }

    @Override
    public void onDestroyView() {
        super.onDestroyView();
        // Set the binding to null to free up resources
        binding = null;
    }
}