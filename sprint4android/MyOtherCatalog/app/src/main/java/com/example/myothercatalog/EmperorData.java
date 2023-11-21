package com.example.myothercatalog;

import org.json.JSONException;
import org.json.JSONObject;

public class EmperorData {
    private String name;
    private String description;
    private String imageUrl;
    public EmperorData(String name, String description, String imageUrl){
        this.name = name;
        this.description = description;
        this.imageUrl = imageUrl;
    }
    public EmperorData(JSONObject json){
        try{
            this.name = json.getString("name");
            this.description = json.getString("description");
            this.imageUrl = json.getString("image_url");
        }catch (JSONException e){
            e.printStackTrace();
        }
    }
    public String getName() {return name;}
    public String getDescription() {return description;}
    public String getImageUrl() {return imageUrl;};
}
