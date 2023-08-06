# Social Finance Data Pipeline

This is a package that aims to standerdise one or more datasets against a defined schema.
It is currently in it's very early stagies.

check the [wiki](https://github.com/SocialFinanceDigitalLabs/sfdata/wiki) for more details on the plan.


## Current status


Current the pipeline only works with xml files and is limited to one schema and one file.
It's a first generic approach, that was tested against CIN and SWWF datasets.

It covers partially the following steps described in the [wiki](https://github.com/SocialFinanceDigitalLabs/sfdata/wiki):
- **Identify** - identifies the stream of data against the schema. only for XML files for now.
- **Convert** - Tries to converts the datatypes and throws a warning when not possible. It uses the [xsdata](https://xsdata.readthedocs.io/en/latest/xml.html) package for it.
- **Normalise** - adds the primary and foreign keys for each record.


## How to run

Check the [demo.py](./demo.py) file. It has 2 functions that run against the CIN and SWWF datasets present in the [samples](./samples/) directory.

There's also smaller samples of those datasets.

This methods will print a set of dataframes for each dataset.
## Improvements

There's still a lot to be done. Besides completing what's in the wiki, here are some things I believe should be done first:

- **Datastore** - the values are directly pulled to a tablib databook in a very unneficcient nested for loop. This is a big **no**. We should use [RTOF datstore](https://github.com/SocialFinanceDigitalLabs/rtof-infrastructure/tree/main/sfdata_datastore) for this.

- **Datatypes** It should be possible to define the way we want to export the datatypes. maybe the user wants the dates to come out in a the "dd-mm-yyyy" format when exporting. Or maybe they want just mm-yyyy. This should be possible. Currently, I'm assuming this in [export_value](./sfdata/exporter.py). But it should be adjusted.

- **path** vs **context** - I was using path as a reference for where the each node sits in the hierarchy. However, having a tuple in the context is probably a better approach. I'm currently using both, this should not be the case - use just the context.

- 


