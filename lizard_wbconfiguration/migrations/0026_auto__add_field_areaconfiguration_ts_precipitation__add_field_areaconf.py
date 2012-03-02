# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'AreaConfiguration.ts_precipitation'
        db.add_column('lizard_wbconfiguration_areaconfiguration', 'ts_precipitation', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True), keep_default=False)

        # Adding field 'AreaConfiguration.ts_evaporation'
        db.add_column('lizard_wbconfiguration_areaconfiguration', 'ts_evaporation', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True), keep_default=False)

        # Adding field 'AreaConfiguration.ts_concentr_chloride_1'
        db.add_column('lizard_wbconfiguration_areaconfiguration', 'ts_concentr_chloride_1', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True), keep_default=False)

        # Adding field 'AreaConfiguration.ts_concentr_chloride_2'
        db.add_column('lizard_wbconfiguration_areaconfiguration', 'ts_concentr_chloride_2', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True), keep_default=False)

        # Adding field 'AreaConfiguration.ts_water_level'
        db.add_column('lizard_wbconfiguration_areaconfiguration', 'ts_water_level', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True), keep_default=False)

        # Adding field 'AreaConfiguration.ts_kwel'
        db.add_column('lizard_wbconfiguration_areaconfiguration', 'ts_kwel', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True), keep_default=False)

        # Adding field 'AreaConfiguration.ts_wegz'
        db.add_column('lizard_wbconfiguration_areaconfiguration', 'ts_wegz', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True), keep_default=False)

        # Adding field 'AreaConfiguration.ts_sp'
        db.add_column('lizard_wbconfiguration_areaconfiguration', 'ts_sp', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True), keep_default=False)

        # Adding field 'Structure.ts_debiet'
        db.add_column('lizard_wbconfiguration_structure', 'ts_debiet', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True), keep_default=False)

        # Adding field 'Bucket.flowoff_is_ts'
        db.add_column('lizard_wbconfiguration_bucket', 'flowoff_is_ts', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Bucket.flowoff'
        db.add_column('lizard_wbconfiguration_bucket', 'flowoff', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=3, blank=True), keep_default=False)

        # Adding field 'Bucket.ts_flowoff'
        db.add_column('lizard_wbconfiguration_bucket', 'ts_flowoff', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True), keep_default=False)

        # Adding field 'Bucket.drainageindraft_is_ts'
        db.add_column('lizard_wbconfiguration_bucket', 'drainageindraft_is_ts', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Bucket.drainageindraft'
        db.add_column('lizard_wbconfiguration_bucket', 'drainageindraft', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=3, blank=True), keep_default=False)

        # Adding field 'Bucket.ts_drainageindraft'
        db.add_column('lizard_wbconfiguration_bucket', 'ts_drainageindraft', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True), keep_default=False)

        # Adding field 'Bucket.referenceoverflow_is_ts'
        db.add_column('lizard_wbconfiguration_bucket', 'referenceoverflow_is_ts', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Bucket.referenceoverflow'
        db.add_column('lizard_wbconfiguration_bucket', 'referenceoverflow', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=3, blank=True), keep_default=False)

        # Adding field 'Bucket.ts_referenceoverflow'
        db.add_column('lizard_wbconfiguration_bucket', 'ts_referenceoverflow', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True), keep_default=False)

        # Adding field 'Bucket.ts_kwelwegz'
        db.add_column('lizard_wbconfiguration_bucket', 'ts_kwelwegz', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'AreaConfiguration.ts_precipitation'
        db.delete_column('lizard_wbconfiguration_areaconfiguration', 'ts_precipitation')

        # Deleting field 'AreaConfiguration.ts_evaporation'
        db.delete_column('lizard_wbconfiguration_areaconfiguration', 'ts_evaporation')

        # Deleting field 'AreaConfiguration.ts_concentr_chloride_1'
        db.delete_column('lizard_wbconfiguration_areaconfiguration', 'ts_concentr_chloride_1')

        # Deleting field 'AreaConfiguration.ts_concentr_chloride_2'
        db.delete_column('lizard_wbconfiguration_areaconfiguration', 'ts_concentr_chloride_2')

        # Deleting field 'AreaConfiguration.ts_water_level'
        db.delete_column('lizard_wbconfiguration_areaconfiguration', 'ts_water_level')

        # Deleting field 'AreaConfiguration.ts_kwel'
        db.delete_column('lizard_wbconfiguration_areaconfiguration', 'ts_kwel')

        # Deleting field 'AreaConfiguration.ts_wegz'
        db.delete_column('lizard_wbconfiguration_areaconfiguration', 'ts_wegz')

        # Deleting field 'AreaConfiguration.ts_sp'
        db.delete_column('lizard_wbconfiguration_areaconfiguration', 'ts_sp')

        # Deleting field 'Structure.ts_debiet'
        db.delete_column('lizard_wbconfiguration_structure', 'ts_debiet')

        # Deleting field 'Bucket.flowoff_is_ts'
        db.delete_column('lizard_wbconfiguration_bucket', 'flowoff_is_ts')

        # Deleting field 'Bucket.flowoff'
        db.delete_column('lizard_wbconfiguration_bucket', 'flowoff')

        # Deleting field 'Bucket.ts_flowoff'
        db.delete_column('lizard_wbconfiguration_bucket', 'ts_flowoff')

        # Deleting field 'Bucket.drainageindraft_is_ts'
        db.delete_column('lizard_wbconfiguration_bucket', 'drainageindraft_is_ts')

        # Deleting field 'Bucket.drainageindraft'
        db.delete_column('lizard_wbconfiguration_bucket', 'drainageindraft')

        # Deleting field 'Bucket.ts_drainageindraft'
        db.delete_column('lizard_wbconfiguration_bucket', 'ts_drainageindraft')

        # Deleting field 'Bucket.referenceoverflow_is_ts'
        db.delete_column('lizard_wbconfiguration_bucket', 'referenceoverflow_is_ts')

        # Deleting field 'Bucket.referenceoverflow'
        db.delete_column('lizard_wbconfiguration_bucket', 'referenceoverflow')

        # Deleting field 'Bucket.ts_referenceoverflow'
        db.delete_column('lizard_wbconfiguration_bucket', 'ts_referenceoverflow')

        # Deleting field 'Bucket.ts_kwelwegz'
        db.delete_column('lizard_wbconfiguration_bucket', 'ts_kwelwegz')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'lizard_area.area': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Area', '_ormbases': ['lizard_area.Communique']},
            'area_class': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'area_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'communique_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['lizard_area.Communique']", 'unique': 'True', 'primary_key': 'True'}),
            'data_administrator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_area.DataAdministrator']", 'null': 'True', 'blank': 'True'}),
            'data_set': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_security.DataSet']", 'null': 'True', 'blank': 'True'}),
            'dt_created': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 3, 2, 11, 39, 8, 622145)'}),
            'dt_latestchanged': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'dt_latestsynchronized': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_area.Area']", 'null': 'True', 'blank': 'True'})
        },
        'lizard_area.communique': {
            'Meta': {'object_name': 'Communique', '_ormbases': ['lizard_geo.GeoObject']},
            'areasort': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'areasort_krw': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'dt_latestchanged_krw': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'edited_at': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'edited_by': ('django.db.models.fields.TextField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'geoobject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['lizard_geo.GeoObject']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'surface': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '1', 'blank': 'True'}),
            'watertype_krw': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'lizard_area.dataadministrator': {
            'Meta': {'object_name': 'DataAdministrator'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'lizard_geo.geoobject': {
            'Meta': {'object_name': 'GeoObject'},
            'geo_object_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_geo.GeoObjectGroup']"}),
            'geometry': ('django.contrib.gis.db.models.fields.GeometryField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ident': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        'lizard_geo.geoobjectgroup': {
            'Meta': {'object_name': 'GeoObjectGroup'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'source_log': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'lizard_security.dataset': {
            'Meta': {'ordering': "['name']", 'object_name': 'DataSet'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'})
        },
        'lizard_wbconfiguration.areaconfiguration': {
            'Meta': {'object_name': 'AreaConfiguration'},
            'area': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['lizard_area.Area']", 'unique': 'True'}),
            'bottom_height': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'concentr_chloride_precipitation': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'concentr_chloride_seepage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'data_set': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_security.DataSet']", 'null': 'True', 'blank': 'True'}),
            'herfstp': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ident': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'incr_concentr_nitrogyn_precipitation': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'incr_concentr_nitrogyn_seepage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'incr_concentr_phosphate_precipitation': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'incr_concentr_phosphate_seepage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'incr_concentr_so4_precipitation': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'incr_concentr_so4_seepage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'ini_con_cl': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'init_water_level': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'kwel': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'kwel_is_ts': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lentep': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'marge_bov': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'marge_ond': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'max_intake': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'max_outtake': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'min_concentr_nitrogyn_precipitation': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'min_concentr_nitrogyn_seepage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'min_concentr_phopshate_seepage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'min_concentr_phosphate_precipitation': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'min_concentr_so4_precipitation': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'min_concentr_so4_seepage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'nutc_inc_1': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'nutc_inc_2': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'nutc_inc_3': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'nutc_inc_4': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'nutc_min_1': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'nutc_min_2': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'nutc_min_3': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'nutc_min_4': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'peilh_issp': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sp_is_ts': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_dt': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'start_hp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'start_lp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'start_wp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'start_zp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'surface': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '1', 'blank': 'True'}),
            'ts_concentr_chloride_1': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'ts_concentr_chloride_2': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'ts_evaporation': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'ts_kwel': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'ts_precipitation': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'ts_sp': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'ts_water_level': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'ts_wegz': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'wegz': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'wegz_is_ts': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'winterp': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'x': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '9', 'blank': 'True'}),
            'y': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '9', 'blank': 'True'}),
            'zomerp': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'})
        },
        'lizard_wbconfiguration.areafield': {
            'Meta': {'object_name': 'AreaField'},
            'app_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '256', 'primary_key': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'model_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'lizard_wbconfiguration.areagridconfiguration': {
            'Meta': {'object_name': 'AreaGridConfiguration'},
            'app_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'lizard_wbconfiguration.areagridfieldconfiguration': {
            'Meta': {'object_name': 'AreaGridFieldConfiguration'},
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'editable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'field_name': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_wbconfiguration.AreaField']", 'max_length': '128'}),
            'field_type': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'grid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_wbconfiguration.AreaGridConfiguration']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sequence': ('django.db.models.fields.IntegerField', [], {}),
            'ts_parameter': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'lizard_wbconfiguration.bucket': {
            'Meta': {'ordering': "['id']", 'object_name': 'Bucket'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_wbconfiguration.AreaConfiguration']"}),
            'bottom_crop_evaporation_factor': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'bottom_drainage_fraction': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'bottom_equi_water_level': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'bottom_indraft_fraction': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'bottom_init_water_level': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'bottom_max_water_level': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'bottom_min_crop_evaporation_factor': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'bottom_min_water_level': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'bottom_porosity': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'bucket_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_wbconfiguration.BucketsType']", 'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'concentr_chloride_drainage_indraft': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'concentr_chloride_flow_off': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'crop_evaporation_factor': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'data_set': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_security.DataSet']", 'null': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'drainage_fraction': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'drainageindraft': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'drainageindraft_is_ts': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'equi_water_level': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'flowoff': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'flowoff_is_ts': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incr_concentr_nitrogen_drainage_indraft': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'incr_concentr_nitrogen_flow_off': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'incr_concentr_phosphate_drainage_indraft': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'incr_concentr_phosphate_flow_off': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'incr_concentr_so4_drainage_indraft': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'incr_concentr_so4_flow_off': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'indraft_fraction': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'ingebr': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'init_water_level': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'is_computed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'kwelwegz': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'kwelwegz_is_ts': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'label_drainaige_indraft': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'label_flow_off': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'man_water_level': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'min_concentr_nitrogen_drainage_indraft': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'min_concentr_nitrogen_flow_off': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'min_concentr_phosphate_drainage_indraft': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'min_concentr_phosphate_flow_off': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'min_concentr_so4_drainage_indraft': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'min_concentr_so4_flow_off': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'min_crop_evaporation_factor': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'min_water_level': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'porosity': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'referenceoverflow': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'referenceoverflow_is_ts': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'replace_impact_by_nutricalc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'surface': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '1', 'blank': 'True'}),
            'ts_drainageindraft': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'ts_flowoff': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'ts_kwelwegz': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'ts_referenceoverflow': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'x': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '9', 'blank': 'True'}),
            'y': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '9', 'blank': 'True'})
        },
        'lizard_wbconfiguration.bucketstype': {
            'Meta': {'object_name': 'BucketsType'},
            'bucket_type': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'code': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'lizard_wbconfiguration.dbfconfiguration': {
            'Meta': {'object_name': 'DBFConfiguration'},
            'data_set': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_security.DataSet']", 'null': 'True', 'blank': 'True'}),
            'dbf_type': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'save_to': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'})
        },
        'lizard_wbconfiguration.structure': {
            'Meta': {'ordering': "['id']", 'object_name': 'Structure'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_wbconfiguration.AreaConfiguration']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'concentr_chloride': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'data_set': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_security.DataSet']", 'null': 'True', 'blank': 'True'}),
            'deb_is_ts': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'deb_wint': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'deb_zomer': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_out': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_wbconfiguration.StructureInOut']", 'null': 'True', 'blank': 'True'}),
            'incr_concentr_nitrogen': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'incr_concentr_phosphate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'incr_concentr_so4': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'ingebr': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_computed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'min_concentr_nitrogen': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'min_concentr_phosphate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'min_concentr_so4': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '3', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'ts_debiet': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'x': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '9', 'blank': 'True'}),
            'y': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '9', 'blank': 'True'})
        },
        'lizard_wbconfiguration.structureinout': {
            'Meta': {'object_name': 'StructureInOut'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {'max_length': '1'})
        },
        'lizard_wbconfiguration.wbconfigurationdbfmapping': {
            'Meta': {'ordering': "['id']", 'object_name': 'WBConfigurationDBFMapping'},
            'dbffield_decimals': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dbffield_length': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dbffield_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'dbffield_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'model_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'wbfield_name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['lizard_wbconfiguration']
