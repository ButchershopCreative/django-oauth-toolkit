# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

try:
    from django.contrib.auth import get_user_model
except ImportError:  # django < 1.5
    from django.contrib.auth.models import User
else:
    User = get_user_model()


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Application'
        # db.create_table(u'oauth2_provider_application', (
        #     (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        #     ('client_id', self.gf('django.db.models.fields.CharField')(default='284250a821f74df67cb50b6c2b7fc95d39d0e4a9', unique=True, max_length=100)),
        #     ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm["%s.%s" % (User._meta.app_label, User._meta.object_name)])),
        #     ('redirect_uris', self.gf('django.db.models.fields.TextField')(blank=True)),
        #     ('client_type', self.gf('django.db.models.fields.CharField')(max_length=32)),
        #     ('authorization_grant_type', self.gf('django.db.models.fields.CharField')(max_length=32)),
        #     ('client_secret', self.gf('django.db.models.fields.CharField')(default='89288b8343edef095b5fee98b4def28409cf4e064fcd26b00c555f51d8fdabfcaedbae8b9d6739080cf27d216e13cc85133d794c9cc1018e0d116c951f0b865e', max_length=255, blank=True)),
        #     ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        # ))
        # db.send_create_signal(u'oauth2_provider', ['Application'])

        # Adding model 'Grant'
        db.create_table(u'oauth2_provider_grant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm["%s.%s" % (User._meta.app_label, User._meta.object_name)])),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('application', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['oauth2_applications.OAuth2Application'])),
            ('expires', self.gf('django.db.models.fields.DateTimeField')()),
            ('redirect_uri', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('scope', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'oauth2_provider', ['Grant'])

        # Adding model 'AccessToken'
        db.create_table(u'oauth2_provider_accesstoken', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm["%s.%s" % (User._meta.app_label, User._meta.object_name)])),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('application', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['oauth2_applications.OAuth2Application'])),
            ('expires', self.gf('django.db.models.fields.DateTimeField')()),
            ('scope', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'oauth2_provider', ['AccessToken'])

        # Adding model 'RefreshToken'
        db.create_table(u'oauth2_provider_refreshtoken', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm["%s.%s" % (User._meta.app_label, User._meta.object_name)])),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('application', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['oauth2_applications.OAuth2Application'])),
            ('access_token', self.gf('django.db.models.fields.related.OneToOneField')(related_name='refresh_token', unique=True, to=orm['oauth2_provider.AccessToken'])),
        ))
        db.send_create_signal(u'oauth2_provider', ['RefreshToken'])


    def backwards(self, orm):
        # Deleting model 'Application'
        try:
            db.delete_table(u'oauth2_provider_application')
        except:
            pass

        # Deleting model 'Grant'
        db.delete_table(u'oauth2_provider_grant')

        # Deleting model 'AccessToken'
        db.delete_table(u'oauth2_provider_accesstoken')

        # Deleting model 'RefreshToken'
        db.delete_table(u'oauth2_provider_refreshtoken')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u"%s.%s" % (User._meta.app_label, User._meta.object_name): {
            'Meta': {'object_name': User.__name__},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'oauth2_provider.accesstoken': {
            'Meta': {'object_name': 'AccessToken'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oauth2_applications.OAuth2Application']"}),
            'expires': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scope': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['%s.%s']"% (User._meta.app_label, User._meta.object_name)})
        },
        u'oauth2_applications.OAuth2Application': {
            'Meta': {'object_name': 'OAuth2Application'},
            'authorization_grant_type': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'client_id': ('django.db.models.fields.CharField', [], {'default': "u'DF!3-DYzSVKQ05HTA4DLWHh!.0_GnWSlNWsA3O6-'", 'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'client_secret': ('django.db.models.fields.CharField', [], {'default': "u'tGL9Qa9UQKli?rdXhRBHiFk6syAciO.coiDb5j:a-80pp;4bR4wIBo80-FCv-j4vF6iNmVyG=@DcXwty?MAxgCvarMc785!9=SlyJb8u86m6b?-xlNHnAx.p7h!!SRwH'", 'max_length': '255', 'db_index': 'True', 'blank': 'True'}),
            'client_type': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'redirect_uris': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        u'oauth2_provider.grant': {
            'Meta': {'object_name': 'Grant'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oauth2_applications.OAuth2Application']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'expires': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'redirect_uri': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'scope': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['%s.%s']"% (User._meta.app_label, User._meta.object_name)})
        },
        u'oauth2_provider.refreshtoken': {
            'Meta': {'object_name': 'RefreshToken'},
            'access_token': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'refresh_token'", 'unique': 'True', 'to': u"orm['oauth2_provider.AccessToken']"}),
            'application': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oauth2_applications.OAuth2Application']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['%s.%s']"% (User._meta.app_label, User._meta.object_name)})
        }
    }

    complete_apps = ['oauth2_provider']