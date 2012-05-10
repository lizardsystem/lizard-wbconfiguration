# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'AreaConfiguration.nutc_inc_2'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'nutc_inc_2', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'AreaConfiguration.nutc_inc_3'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'nutc_inc_3', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'AreaConfiguration.nutc_inc_1'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'nutc_inc_1', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'AreaConfiguration.min_concentr_phopshate_seepage'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'min_concentr_phopshate_seepage', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'AreaConfiguration.nutc_inc_4'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'nutc_inc_4', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'AreaConfiguration.nutc_min_3'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'nutc_min_3', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'AreaConfiguration.max_outtake'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'max_outtake', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'AreaConfiguration.surface'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'surface', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'AreaConfiguration.marge_bov'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'marge_bov', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'AreaConfiguration.min_concentr_nitrogyn_seepage'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'min_concentr_nitrogyn_seepage', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'AreaConfiguration.min_concentr_so4_seepage'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'min_concentr_so4_seepage', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'AreaConfiguration.init_water_level'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'init_water_level', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'AreaConfiguration.kwel'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'kwel', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'AreaConfiguration.min_concentr_nitrogyn_precipitation'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'min_concentr_nitrogyn_precipitation', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'AreaConfiguration.nutc_min_2'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'nutc_min_2', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'AreaConfiguration.ini_con_cl'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'ini_con_cl', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'AreaConfiguration.wegz'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'wegz', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'AreaConfiguration.nutc_min_4'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'nutc_min_4', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'AreaConfiguration.zomerp'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'zomerp', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'AreaConfiguration.incr_concentr_phosphate_seepage'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'incr_concentr_phosphate_seepage', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'AreaConfiguration.incr_concentr_nitrogyn_seepage'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'incr_concentr_nitrogyn_seepage', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'AreaConfiguration.incr_concentr_so4_precipitation'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'incr_concentr_so4_precipitation', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'AreaConfiguration.incr_concentr_so4_seepage'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'incr_concentr_so4_seepage', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'AreaConfiguration.concentr_chloride_seepage'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'concentr_chloride_seepage', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'AreaConfiguration.min_concentr_so4_precipitation'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'min_concentr_so4_precipitation', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'AreaConfiguration.winterp'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'winterp', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'AreaConfiguration.max_intake'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'max_intake', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'AreaConfiguration.bottom_height'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'bottom_height', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'AreaConfiguration.lentep'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'lentep', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'AreaConfiguration.incr_concentr_nitrogyn_precipitation'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'incr_concentr_nitrogyn_precipitation', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'AreaConfiguration.incr_concentr_phosphate_precipitation'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'incr_concentr_phosphate_precipitation', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'AreaConfiguration.concentr_chloride_precipitation'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'concentr_chloride_precipitation', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'AreaConfiguration.min_concentr_phosphate_precipitation'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'min_concentr_phosphate_precipitation', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'AreaConfiguration.herfstp'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'herfstp', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'AreaConfiguration.marge_ond'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'marge_ond', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'AreaConfiguration.nutc_min_1'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'nutc_min_1', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Structure.concentr_chloride'
        db.alter_column('lizard_wbconfiguration_structure', 'concentr_chloride', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Structure.deb_zomer'
        db.alter_column('lizard_wbconfiguration_structure', 'deb_zomer', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Structure.incr_concentr_so4'
        db.alter_column('lizard_wbconfiguration_structure', 'incr_concentr_so4', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Structure.incr_concentr_nitrogen'
        db.alter_column('lizard_wbconfiguration_structure', 'incr_concentr_nitrogen', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Structure.deb_wint'
        db.alter_column('lizard_wbconfiguration_structure', 'deb_wint', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Structure.min_concentr_so4'
        db.alter_column('lizard_wbconfiguration_structure', 'min_concentr_so4', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Structure.min_concentr_phosphate'
        db.alter_column('lizard_wbconfiguration_structure', 'min_concentr_phosphate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Structure.min_concentr_nitrogen'
        db.alter_column('lizard_wbconfiguration_structure', 'min_concentr_nitrogen', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Structure.incr_concentr_phosphate'
        db.alter_column('lizard_wbconfiguration_structure', 'incr_concentr_phosphate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.drainage_fraction'
        db.alter_column('lizard_wbconfiguration_bucket', 'drainage_fraction', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.concentr_chloride_drainage_indraft'
        db.alter_column('lizard_wbconfiguration_bucket', 'concentr_chloride_drainage_indraft', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.init_water_level'
        db.alter_column('lizard_wbconfiguration_bucket', 'init_water_level', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.concentr_chloride_flow_off'
        db.alter_column('lizard_wbconfiguration_bucket', 'concentr_chloride_flow_off', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.surface'
        db.alter_column('lizard_wbconfiguration_bucket', 'surface', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.incr_concentr_phosphate_flow_off'
        db.alter_column('lizard_wbconfiguration_bucket', 'incr_concentr_phosphate_flow_off', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.bottom_equi_water_level'
        db.alter_column('lizard_wbconfiguration_bucket', 'bottom_equi_water_level', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.incr_concentr_so4_drainage_indraft'
        db.alter_column('lizard_wbconfiguration_bucket', 'incr_concentr_so4_drainage_indraft', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.incr_concentr_phosphate_drainage_indraft'
        db.alter_column('lizard_wbconfiguration_bucket', 'incr_concentr_phosphate_drainage_indraft', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.min_concentr_nitrogen_flow_off'
        db.alter_column('lizard_wbconfiguration_bucket', 'min_concentr_nitrogen_flow_off', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.drainageindraft'
        db.alter_column('lizard_wbconfiguration_bucket', 'drainageindraft', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.referenceoverflow'
        db.alter_column('lizard_wbconfiguration_bucket', 'referenceoverflow', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.min_concentr_phosphate_flow_off'
        db.alter_column('lizard_wbconfiguration_bucket', 'min_concentr_phosphate_flow_off', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.equi_water_level'
        db.alter_column('lizard_wbconfiguration_bucket', 'equi_water_level', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.bottom_drainage_fraction'
        db.alter_column('lizard_wbconfiguration_bucket', 'bottom_drainage_fraction', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.incr_concentr_so4_flow_off'
        db.alter_column('lizard_wbconfiguration_bucket', 'incr_concentr_so4_flow_off', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.bottom_init_water_level'
        db.alter_column('lizard_wbconfiguration_bucket', 'bottom_init_water_level', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.min_concentr_nitrogen_drainage_indraft'
        db.alter_column('lizard_wbconfiguration_bucket', 'min_concentr_nitrogen_drainage_indraft', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.label_flow_off'
        db.alter_column('lizard_wbconfiguration_bucket', 'label_flow_off', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.min_water_level'
        db.alter_column('lizard_wbconfiguration_bucket', 'min_water_level', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.porosity'
        db.alter_column('lizard_wbconfiguration_bucket', 'porosity', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.bottom_max_water_level'
        db.alter_column('lizard_wbconfiguration_bucket', 'bottom_max_water_level', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.bottom_indraft_fraction'
        db.alter_column('lizard_wbconfiguration_bucket', 'bottom_indraft_fraction', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.min_concentr_phosphate_drainage_indraft'
        db.alter_column('lizard_wbconfiguration_bucket', 'min_concentr_phosphate_drainage_indraft', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.bottom_porosity'
        db.alter_column('lizard_wbconfiguration_bucket', 'bottom_porosity', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.bottom_min_water_level'
        db.alter_column('lizard_wbconfiguration_bucket', 'bottom_min_water_level', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.label_drainaige_indraft'
        db.alter_column('lizard_wbconfiguration_bucket', 'label_drainaige_indraft', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.incr_concentr_nitrogen_drainage_indraft'
        db.alter_column('lizard_wbconfiguration_bucket', 'incr_concentr_nitrogen_drainage_indraft', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.min_concentr_so4_flow_off'
        db.alter_column('lizard_wbconfiguration_bucket', 'min_concentr_so4_flow_off', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.min_crop_evaporation_factor'
        db.alter_column('lizard_wbconfiguration_bucket', 'min_crop_evaporation_factor', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.man_water_level'
        db.alter_column('lizard_wbconfiguration_bucket', 'man_water_level', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.flowoff'
        db.alter_column('lizard_wbconfiguration_bucket', 'flowoff', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.incr_concentr_nitrogen_flow_off'
        db.alter_column('lizard_wbconfiguration_bucket', 'incr_concentr_nitrogen_flow_off', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.kwelwegz'
        db.alter_column('lizard_wbconfiguration_bucket', 'kwelwegz', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.bottom_crop_evaporation_factor'
        db.alter_column('lizard_wbconfiguration_bucket', 'bottom_crop_evaporation_factor', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.indraft_fraction'
        db.alter_column('lizard_wbconfiguration_bucket', 'indraft_fraction', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.min_concentr_so4_drainage_indraft'
        db.alter_column('lizard_wbconfiguration_bucket', 'min_concentr_so4_drainage_indraft', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.crop_evaporation_factor'
        db.alter_column('lizard_wbconfiguration_bucket', 'crop_evaporation_factor', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))

        # Changing field 'Bucket.bottom_min_crop_evaporation_factor'
        db.alter_column('lizard_wbconfiguration_bucket', 'bottom_min_crop_evaporation_factor', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=5))


    def backwards(self, orm):
        
        # Changing field 'AreaConfiguration.nutc_inc_2'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'nutc_inc_2', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2))

        # Changing field 'AreaConfiguration.nutc_inc_3'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'nutc_inc_3', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2))

        # Changing field 'AreaConfiguration.nutc_inc_1'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'nutc_inc_1', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2))

        # Changing field 'AreaConfiguration.min_concentr_phopshate_seepage'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'min_concentr_phopshate_seepage', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2))

        # Changing field 'AreaConfiguration.nutc_inc_4'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'nutc_inc_4', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2))

        # Changing field 'AreaConfiguration.nutc_min_3'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'nutc_min_3', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2))

        # Changing field 'AreaConfiguration.max_outtake'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'max_outtake', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'AreaConfiguration.surface'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'surface', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=0))

        # Changing field 'AreaConfiguration.marge_bov'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'marge_bov', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'AreaConfiguration.min_concentr_nitrogyn_seepage'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'min_concentr_nitrogyn_seepage', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2))

        # Changing field 'AreaConfiguration.min_concentr_so4_seepage'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'min_concentr_so4_seepage', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2))

        # Changing field 'AreaConfiguration.init_water_level'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'init_water_level', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2))

        # Changing field 'AreaConfiguration.kwel'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'kwel', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'AreaConfiguration.min_concentr_nitrogyn_precipitation'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'min_concentr_nitrogyn_precipitation', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2))

        # Changing field 'AreaConfiguration.nutc_min_2'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'nutc_min_2', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2))

        # Changing field 'AreaConfiguration.ini_con_cl'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'ini_con_cl', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2))

        # Changing field 'AreaConfiguration.wegz'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'wegz', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'AreaConfiguration.nutc_min_4'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'nutc_min_4', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2))

        # Changing field 'AreaConfiguration.zomerp'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'zomerp', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2))

        # Changing field 'AreaConfiguration.incr_concentr_phosphate_seepage'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'incr_concentr_phosphate_seepage', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2))

        # Changing field 'AreaConfiguration.incr_concentr_nitrogyn_seepage'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'incr_concentr_nitrogyn_seepage', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2))

        # Changing field 'AreaConfiguration.incr_concentr_so4_precipitation'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'incr_concentr_so4_precipitation', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2))

        # Changing field 'AreaConfiguration.incr_concentr_so4_seepage'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'incr_concentr_so4_seepage', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2))

        # Changing field 'AreaConfiguration.concentr_chloride_seepage'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'concentr_chloride_seepage', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2))

        # Changing field 'AreaConfiguration.min_concentr_so4_precipitation'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'min_concentr_so4_precipitation', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2))

        # Changing field 'AreaConfiguration.winterp'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'winterp', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2))

        # Changing field 'AreaConfiguration.max_intake'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'max_intake', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'AreaConfiguration.bottom_height'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'bottom_height', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'AreaConfiguration.lentep'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'lentep', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2))

        # Changing field 'AreaConfiguration.incr_concentr_nitrogyn_precipitation'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'incr_concentr_nitrogyn_precipitation', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2))

        # Changing field 'AreaConfiguration.incr_concentr_phosphate_precipitation'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'incr_concentr_phosphate_precipitation', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2))

        # Changing field 'AreaConfiguration.concentr_chloride_precipitation'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'concentr_chloride_precipitation', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2))

        # Changing field 'AreaConfiguration.min_concentr_phosphate_precipitation'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'min_concentr_phosphate_precipitation', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2))

        # Changing field 'AreaConfiguration.herfstp'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'herfstp', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2))

        # Changing field 'AreaConfiguration.marge_ond'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'marge_ond', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'AreaConfiguration.nutc_min_1'
        db.alter_column('lizard_wbconfiguration_areaconfiguration', 'nutc_min_1', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2))

        # Changing field 'Structure.concentr_chloride'
        db.alter_column('lizard_wbconfiguration_structure', 'concentr_chloride', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Structure.deb_zomer'
        db.alter_column('lizard_wbconfiguration_structure', 'deb_zomer', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Structure.incr_concentr_so4'
        db.alter_column('lizard_wbconfiguration_structure', 'incr_concentr_so4', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Structure.incr_concentr_nitrogen'
        db.alter_column('lizard_wbconfiguration_structure', 'incr_concentr_nitrogen', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Structure.deb_wint'
        db.alter_column('lizard_wbconfiguration_structure', 'deb_wint', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Structure.min_concentr_so4'
        db.alter_column('lizard_wbconfiguration_structure', 'min_concentr_so4', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Structure.min_concentr_phosphate'
        db.alter_column('lizard_wbconfiguration_structure', 'min_concentr_phosphate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Structure.min_concentr_nitrogen'
        db.alter_column('lizard_wbconfiguration_structure', 'min_concentr_nitrogen', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Structure.incr_concentr_phosphate'
        db.alter_column('lizard_wbconfiguration_structure', 'incr_concentr_phosphate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.drainage_fraction'
        db.alter_column('lizard_wbconfiguration_bucket', 'drainage_fraction', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.concentr_chloride_drainage_indraft'
        db.alter_column('lizard_wbconfiguration_bucket', 'concentr_chloride_drainage_indraft', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.init_water_level'
        db.alter_column('lizard_wbconfiguration_bucket', 'init_water_level', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.concentr_chloride_flow_off'
        db.alter_column('lizard_wbconfiguration_bucket', 'concentr_chloride_flow_off', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.surface'
        db.alter_column('lizard_wbconfiguration_bucket', 'surface', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=0))

        # Changing field 'Bucket.incr_concentr_phosphate_flow_off'
        db.alter_column('lizard_wbconfiguration_bucket', 'incr_concentr_phosphate_flow_off', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.bottom_equi_water_level'
        db.alter_column('lizard_wbconfiguration_bucket', 'bottom_equi_water_level', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.incr_concentr_so4_drainage_indraft'
        db.alter_column('lizard_wbconfiguration_bucket', 'incr_concentr_so4_drainage_indraft', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.incr_concentr_phosphate_drainage_indraft'
        db.alter_column('lizard_wbconfiguration_bucket', 'incr_concentr_phosphate_drainage_indraft', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.min_concentr_nitrogen_flow_off'
        db.alter_column('lizard_wbconfiguration_bucket', 'min_concentr_nitrogen_flow_off', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.drainageindraft'
        db.alter_column('lizard_wbconfiguration_bucket', 'drainageindraft', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.referenceoverflow'
        db.alter_column('lizard_wbconfiguration_bucket', 'referenceoverflow', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.min_concentr_phosphate_flow_off'
        db.alter_column('lizard_wbconfiguration_bucket', 'min_concentr_phosphate_flow_off', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.equi_water_level'
        db.alter_column('lizard_wbconfiguration_bucket', 'equi_water_level', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.bottom_drainage_fraction'
        db.alter_column('lizard_wbconfiguration_bucket', 'bottom_drainage_fraction', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.incr_concentr_so4_flow_off'
        db.alter_column('lizard_wbconfiguration_bucket', 'incr_concentr_so4_flow_off', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.bottom_init_water_level'
        db.alter_column('lizard_wbconfiguration_bucket', 'bottom_init_water_level', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.min_concentr_nitrogen_drainage_indraft'
        db.alter_column('lizard_wbconfiguration_bucket', 'min_concentr_nitrogen_drainage_indraft', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.label_flow_off'
        db.alter_column('lizard_wbconfiguration_bucket', 'label_flow_off', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.min_water_level'
        db.alter_column('lizard_wbconfiguration_bucket', 'min_water_level', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.porosity'
        db.alter_column('lizard_wbconfiguration_bucket', 'porosity', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.bottom_max_water_level'
        db.alter_column('lizard_wbconfiguration_bucket', 'bottom_max_water_level', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.bottom_indraft_fraction'
        db.alter_column('lizard_wbconfiguration_bucket', 'bottom_indraft_fraction', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.min_concentr_phosphate_drainage_indraft'
        db.alter_column('lizard_wbconfiguration_bucket', 'min_concentr_phosphate_drainage_indraft', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.bottom_porosity'
        db.alter_column('lizard_wbconfiguration_bucket', 'bottom_porosity', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.bottom_min_water_level'
        db.alter_column('lizard_wbconfiguration_bucket', 'bottom_min_water_level', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.label_drainaige_indraft'
        db.alter_column('lizard_wbconfiguration_bucket', 'label_drainaige_indraft', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.incr_concentr_nitrogen_drainage_indraft'
        db.alter_column('lizard_wbconfiguration_bucket', 'incr_concentr_nitrogen_drainage_indraft', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.min_concentr_so4_flow_off'
        db.alter_column('lizard_wbconfiguration_bucket', 'min_concentr_so4_flow_off', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.min_crop_evaporation_factor'
        db.alter_column('lizard_wbconfiguration_bucket', 'min_crop_evaporation_factor', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.man_water_level'
        db.alter_column('lizard_wbconfiguration_bucket', 'man_water_level', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.flowoff'
        db.alter_column('lizard_wbconfiguration_bucket', 'flowoff', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.incr_concentr_nitrogen_flow_off'
        db.alter_column('lizard_wbconfiguration_bucket', 'incr_concentr_nitrogen_flow_off', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.kwelwegz'
        db.alter_column('lizard_wbconfiguration_bucket', 'kwelwegz', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.bottom_crop_evaporation_factor'
        db.alter_column('lizard_wbconfiguration_bucket', 'bottom_crop_evaporation_factor', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.indraft_fraction'
        db.alter_column('lizard_wbconfiguration_bucket', 'indraft_fraction', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.min_concentr_so4_drainage_indraft'
        db.alter_column('lizard_wbconfiguration_bucket', 'min_concentr_so4_drainage_indraft', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.crop_evaporation_factor'
        db.alter_column('lizard_wbconfiguration_bucket', 'crop_evaporation_factor', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Bucket.bottom_min_crop_evaporation_factor'
        db.alter_column('lizard_wbconfiguration_bucket', 'bottom_min_crop_evaporation_factor', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))


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
            'communique_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['lizard_area.Communique']", 'unique': 'True', 'primary_key': 'True'}),
            'data_administrator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_area.DataAdministrator']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_area.Area']", 'null': 'True', 'blank': 'True'})
        },
        'lizard_area.areacode': {
            'Meta': {'object_name': 'AreaCode'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'lizard_area.areatype': {
            'Meta': {'object_name': 'AreaType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'lizard_area.basin': {
            'Meta': {'object_name': 'Basin'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'lizard_area.communique': {
            'Meta': {'object_name': 'Communique', '_ormbases': ['lizard_geo.GeoObject']},
            'area_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_area.AreaType']", 'null': 'True', 'blank': 'True'}),
            'basin': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_area.Basin']", 'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_area.AreaCode']", 'null': 'True', 'blank': 'True'}),
            'geoobject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['lizard_geo.GeoObject']", 'unique': 'True', 'primary_key': 'True'}),
            'municipality': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_area.Municipality']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_area.Province']", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_area.Status']", 'null': 'True', 'blank': 'True'}),
            'watermanagementarea': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_area.WaterManagementArea']", 'null': 'True', 'blank': 'True'})
        },
        'lizard_area.dataadministrator': {
            'Meta': {'object_name': 'DataAdministrator'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'lizard_area.municipality': {
            'Meta': {'object_name': 'Municipality'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'lizard_area.province': {
            'Meta': {'object_name': 'Province'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'lizard_area.status': {
            'Meta': {'object_name': 'Status'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'lizard_area.watermanagementarea': {
            'Meta': {'object_name': 'WaterManagementArea'},
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
            'bottom_height': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'concentr_chloride_precipitation': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'concentr_chloride_seepage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'data_set': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_security.DataSet']", 'null': 'True', 'blank': 'True'}),
            'fews_meta_info': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'herfstp': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ident': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'incr_concentr_nitrogyn_precipitation': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'incr_concentr_nitrogyn_seepage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'incr_concentr_phosphate_precipitation': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'incr_concentr_phosphate_seepage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'incr_concentr_so4_precipitation': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'incr_concentr_so4_seepage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'ini_con_cl': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'init_water_level': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'kwel': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'kwel_is_ts': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lentep': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'marge_bov': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'marge_ond': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'max_intake': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'max_outtake': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'min_concentr_nitrogyn_precipitation': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'min_concentr_nitrogyn_seepage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'min_concentr_phopshate_seepage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'min_concentr_phosphate_precipitation': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'min_concentr_so4_precipitation': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'min_concentr_so4_seepage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'nutc_inc_1': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'nutc_inc_2': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'nutc_inc_3': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'nutc_inc_4': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'nutc_min_1': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'nutc_min_2': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'nutc_min_3': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'nutc_min_4': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'peilh_issp': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sp_is_ts': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_dt': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'start_hp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'start_lp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'start_wp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'start_zp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'surface': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'ts_cl': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'ts_concentr_chloride_1': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'ts_concentr_chloride_2': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'ts_evaporation': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'ts_kwel': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'ts_precipitation': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'ts_sp': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'ts_water_level': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'ts_wegz': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'wegz': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'wegz_is_ts': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'winterp': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'x': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '9', 'blank': 'True'}),
            'y': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '9', 'blank': 'True'}),
            'zomerp': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'})
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
            'bottom_crop_evaporation_factor': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'bottom_drainage_fraction': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'bottom_equi_water_level': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'bottom_indraft_fraction': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'bottom_init_water_level': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'bottom_max_water_level': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'bottom_min_crop_evaporation_factor': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'bottom_min_water_level': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'bottom_porosity': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'bucket_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_wbconfiguration.BucketsType']", 'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'concentr_chloride_drainage_indraft': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'concentr_chloride_flow_off': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'crop_evaporation_factor': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'data_set': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_security.DataSet']", 'null': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'drainage_fraction': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'drainageindraft': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'drainageindraft_is_ts': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'equi_water_level': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'fews_meta_info': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'flowoff': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'flowoff_is_ts': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incr_concentr_nitrogen_drainage_indraft': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'incr_concentr_nitrogen_flow_off': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'incr_concentr_phosphate_drainage_indraft': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'incr_concentr_phosphate_flow_off': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'incr_concentr_so4_drainage_indraft': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'incr_concentr_so4_flow_off': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'indraft_fraction': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'ingebr': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'init_water_level': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'is_computed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'kwelwegz': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'kwelwegz_is_ts': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'label_drainaige_indraft': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'label_flow_off': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'man_water_level': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'min_concentr_nitrogen_drainage_indraft': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'min_concentr_nitrogen_flow_off': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'min_concentr_phosphate_drainage_indraft': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'min_concentr_phosphate_flow_off': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'min_concentr_so4_drainage_indraft': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'min_concentr_so4_flow_off': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'min_crop_evaporation_factor': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'min_water_level': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'porosity': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'referenceoverflow': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'referenceoverflow_is_ts': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'replace_impact_by_nutricalc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'surface': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
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
            'concentr_chloride': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'data_set': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_security.DataSet']", 'null': 'True', 'blank': 'True'}),
            'deb_is_ts': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'deb_wint': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'deb_zomer': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fews_meta_info': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_out': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lizard_wbconfiguration.StructureInOut']", 'null': 'True', 'blank': 'True'}),
            'incr_concentr_nitrogen': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'incr_concentr_phosphate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'incr_concentr_so4': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'ingebr': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_computed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'min_concentr_nitrogen': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'min_concentr_phosphate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'min_concentr_so4': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '5', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'ts_debiet': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'x': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '9', 'blank': 'True'}),
            'y': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '9', 'blank': 'True'})
        },
        'lizard_wbconfiguration.structureinout': {
            'Meta': {'object_name': 'StructureInOut'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
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
