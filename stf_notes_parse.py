#!/usr/bin/env python

import headspin.db as db
import headspin.model.device_note_model as dm
import headspin.model.pool_model as pm

saved_pools = {}
def get_pool_name(pool_id):
    if saved_pools.get(pool_id) is not None:
        return saved_pools[pool_id]

    pool = pm.get_pool(pool_id)
    name = None
    if pool is not None:
        name = pool.pool_internal_name
    saved_pools[pool_id] = name
    return name


with db.db() as (_, cursor):
    notes = dm._get_device_notes(cursor, "note LIKE '%tether_index%'")
    print("Got {} notes".format(len(notes)))
    for note in notes:
        pool = note.pool_id
        pool_name = get_pool_name(pool)
        print("Device {} host {} pool {} ({}) note '{}'".format(note.device_id, note.hostname, pool, pool_name, note.note))
