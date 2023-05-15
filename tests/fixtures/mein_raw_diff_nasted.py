nest_diff = {
  ('group2', 'deleted'): {
    'abc': 12345,
    'deep': {
      'id': 45
    }
  },
  ('group3', 'added'): {
    'deep': {
      'id': {
        'number': 45
      }
    },
    'fee': 100500
  },
  ('common', 'nesting'): {
    ('setting2', 'deleted'): 200,
    ('setting5', 'added'): {
      'key5': 'value5'
    },
    ('setting4', 'added'): 'blah blah',
    ('follow', 'added'): False,
    ('setting3', 'changed_from'): True,
    ('setting3', 'changed_to'): None,
    ('setting1', 'same'): 'Value 1',
    ('setting6', 'nesting'): {
      ('ops', 'added'): 'vops',
      ('doge', 'nesting'): {
        ('wow', 'changed_from'): '',
        ('wow', 'changed_to'): 'so much'
      },
      ('key', 'same'): 'value'
    }
  },
  ('group1', 'nesting'): {
    ('nest', 'changed_from'): {
      'key': 'value'
    },
    ('nest', 'changed_to'): 'str',
    ('foo', 'same'): 'bar',
    ('baz', 'changed_from'): 'bas',
    ('baz', 'changed_to'): 'bars'
  }
}
