package com.example.searchpage

import android.os.Bundle
import com.google.android.material.snackbar.Snackbar
import androidx.appcompat.app.AppCompatActivity
import androidx.navigation.findNavController
import androidx.navigation.ui.AppBarConfiguration
import androidx.navigation.ui.navigateUp
import androidx.navigation.ui.setupActionBarWithNavController
import android.view.Menu
import android.view.MenuItem
import android.widget.AdapterView
import android.widget.ArrayAdapter
import android.widget.SearchView
import android.widget.Toast
import com.example.searchpage.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    private lateinit var adapter: ArrayAdapter<*>
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        adapter = ArrayAdapter(
            this,
            android.R.layout.simple_list_item_1,
            resources.getStringArray(R.array.countries_array)
        )
        lv_listView.adapter = adapter



        lv_listView.adapter = adapter
        lv_listView.onItemClicklistener =
            AdapterView.OnItemClickListener { parent, view, position, id ->
                Toast.makeText(
                    applicationContext,
                    parent?.getItemAtPosition(position).toString(),
                    Toast.LENGTH_SHORT
                ).show()
            }
        lv_listView.emptyView = tv_emptyTextView
    }
    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        menuInflater.inflate (R.menu.menu_main, menu)

        val search : MenuItem? = menu?. findItem(R. id.nav_search)
        val searchView: SearchView = search?.actionView as SearchView
        searchView.queryHint = "Search something!"

        searchView.setOnQueryTextListener(object: SearchView.OnQueryTextListener {
            override fun onQueryTextSubmit(query: String?): Boolean {
                return false
            }

            override fun onQueryTextChange(newText: String?): Boolean {
                adapter.filter.filter(newText)
                return true
            }
        })
            return super.onCreateOptionsMenu(menu)
    }
}