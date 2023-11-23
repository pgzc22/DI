package com.example.myothercatalog;

// Importing necessary libraries
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.app.Activity;
import android.os.Bundle;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;


// Main activity class that extends AppCompatActivity
public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        // Initializing RecyclerView
        RecyclerView recyclerView = findViewById(R.id.recycler_view);
        Activity activity = this;
        // Creating a new JsonArrayRequest to get JSON data from a URL
        JsonArrayRequest request = requestArray (recyclerView, activity);
        // Creating a RequestQueue
        RequestQueue cola = Volley.newRequestQueue(this);
        // Adding the request to the RequestQueue
        cola.add(request);
    }
    public JsonArrayRequest requestArray (RecyclerView recyclerView, Activity activity) {
        return new JsonArrayRequest(
                Request.Method.GET,
                "https://raw.githubusercontent.com/pgzc22/DI/master/catalog.json",
                null,
                new Response.Listener<JSONArray>() {
                    @Override
                    public void onResponse(JSONArray response) {
                        // Creating a list to store the EmperorData
                        List<EmperorData> allTheEmperors = new ArrayList<>();
                        for (int i = 0; i < response.length(); i++) {
                            try {
                                // Getting each emperor object
                                JSONObject emperor = response.getJSONObject(i);
                                // Creating a new EmperorData object
                                EmperorData data = new EmperorData(emperor);
                                // Adding the EmperorData object to the list
                                allTheEmperors.add(data);
                            } catch (JSONException e) {
                                e.printStackTrace();
                            }
                        }
                        // Setting the adapter and layout manager for the RecyclerView
                        EmperorRecyclerViewAdapter adapter = new EmperorRecyclerViewAdapter(allTheEmperors, activity);
                        recyclerView.setAdapter(adapter);
                        recyclerView.setLayoutManager(new LinearLayoutManager(activity));
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        // Displaying error message as a toast
                        Toast.makeText(activity, error.getMessage(), Toast.LENGTH_SHORT).show();
                    }
                }
        );
    }
}