## Benchmark for [this](https://github.com/django-import-export/django-import-export/pull/473)

### The expected behavior:

Use the imported data totally. Not keep old data.


The are two way to do this:

1.  override `before_import` and `get_or_init_instance`.
2.  using the new option: `bulk_repace`

in file [myapp/admin.py](myapp/admin.py), 

`ResourceTestModel_1` is the first way.

`ResourceTestModel_2` is the second way.



### Benchmark

`TestModel-2016-06-20.xls` is the test data which contains 10K rows.

using mysql database. (`pymysql` as driver).


this is the runserver log:

1.  First way

```
[TIME MEASURE] /admin/myapp/testmodel/import/: 11.0680501461
[20/Jun/2016 10:16:32] "POST /admin/myapp/testmodel/import/ HTTP/1.1" 200 5599231
[TIME MEASURE] /admin/myapp/testmodel/process_import/: 96.4507160187
[20/Jun/2016 10:18:20] "POST /admin/myapp/testmodel/process_import/ HTTP/1.1" 302 0
[TIME MEASURE] /admin/myapp/testmodel/: 0.127159118652
[20/Jun/2016 10:18:20] "GET /admin/myapp/testmodel/ HTTP/1.1" 200 46114
```

Total cost 107 seconds.

2.  Second way

```
[TIME MEASURE] /admin/myapp/testmodel/import/: 1.76946806908
[20/Jun/2016 10:19:20] "POST /admin/myapp/testmodel/import/ HTTP/1.1" 302 0
[TIME MEASURE] /admin/myapp/testmodel/: 0.116591215134
[20/Jun/2016 10:19:20] "GET /admin/myapp/testmodel/ HTTP/1.1" 200 45954
```

Total cost 1.8 seconds.


#### The way 2 (using `bulk_replace` option) is about 60 times faster than way 1.

