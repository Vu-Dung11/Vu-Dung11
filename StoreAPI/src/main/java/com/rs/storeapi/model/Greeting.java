package com.rs.storeapi.model;


import lombok.Builder;
import lombok.Data;

@Data
// add lombok for generate all the constructor
@Builder
public class Greeting
{

    private long id;

    private String content;


}
