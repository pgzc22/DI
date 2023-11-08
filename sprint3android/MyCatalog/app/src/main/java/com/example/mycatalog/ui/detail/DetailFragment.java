package com.example.mycatalog.ui.detail;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;

import com.example.mycatalog.databinding.FragmentDetailBinding;
// Define the AboutFragment class that extends Fragment
public class DetailFragment extends Fragment {

    private FragmentDetailBinding binding;

    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {

        // Inflate the layout for this fragment using FragmentAboutBinding
        binding = FragmentDetailBinding.inflate(inflater, container, false);
        // Get the root view of the inflated layout
        View root = binding.getRoot();
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