# Generated by Django 5.0.6 on 2024-07-25 08:08

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('opportunity', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DecisionLog',
            fields=[
                ('id', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('impact', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], default='Low', max_length=20)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Implemented', 'Implemented')], default='Pending', max_length=50)),
                ('details', models.TextField(blank=True, null=True)),
                ('resulting_action', models.TextField(blank=True, null=True)),
                ('proposed_date', models.DateField(blank=True, null=True)),
                ('proposed_by', models.CharField(blank=True, max_length=150, null=True)),
                ('approved_by', models.CharField(blank=True, max_length=150, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'project_decision_log',
            },
        ),
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('risk_category', models.CharField(max_length=100)),
                ('probability', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('impact', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('severity', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(25)])),
                ('risk_owner', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('mitigation_actions', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'project_risk',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('objective', models.TextField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=150, null=True)),
                ('product_owner', models.CharField(blank=True, max_length=150, null=True)),
                ('scrum_master', models.CharField(blank=True, max_length=150, null=True)),
                ('project_sponsor', models.CharField(blank=True, max_length=150, null=True)),
                ('project_manager', models.CharField(blank=True, max_length=150, null=True)),
                ('general_manager', models.CharField(blank=True, max_length=150, null=True)),
                ('development_sponsor', models.CharField(blank=True, max_length=150, null=True)),
                ('phase', models.CharField(choices=[('Ideation', 'Ideation'), ('Scope', 'Scope'), ('Planning', 'Planning'), ('Development', 'Development'), ('Realisation', 'Realisation'), ('Review', 'Review'), ('Closure', 'Closure')], default='Ideation', max_length=20)),
                ('baseline_delivery_date', models.CharField(blank=True, max_length=100, null=True)),
                ('actual_delivery_date', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Completed', 'Completed')], default='Active', max_length=10)),
                ('scope', models.CharField(choices=[('R', 'Red'), ('A', 'Amber'), ('G', 'Green')], default='A', max_length=10)),
                ('cost', models.CharField(choices=[('R', 'Red'), ('A', 'Amber'), ('G', 'Green')], default='A', max_length=10)),
                ('quality', models.CharField(choices=[('R', 'Red'), ('A', 'Amber'), ('G', 'Green')], default='A', max_length=10)),
                ('time', models.CharField(choices=[('R', 'Red'), ('A', 'Amber'), ('G', 'Green')], default='A', max_length=10)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('opportunity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='opportunity.opportunity')),
                ('team_member', models.ManyToManyField(related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'project',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Costs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=150, null=True)),
                ('group', models.CharField(blank=True, max_length=150, null=True)),
                ('budget', models.CharField(blank=True, max_length=150, null=True)),
                ('spent', models.CharField(blank=True, max_length=150, null=True)),
                ('remaining_budget', models.CharField(blank=True, max_length=150, null=True)),
                ('spend_to_finish', models.CharField(blank=True, max_length=150, null=True)),
                ('forecast', models.CharField(blank=True, max_length=150, null=True)),
                ('variance', models.CharField(blank=True, max_length=150, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
            options={
                'db_table': 'project_cost',
            },
        ),
        migrations.CreateModel(
            name='ProjectFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clarity_of_communication', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('responsiveness', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('collaboration', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('deliverable_quality', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('attention_to_detail', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('testing_and_validation', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('adherence_to_deadlines', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('time_management', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('knowledge_and_skills', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('problem_solving', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('overall_satisfaction', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('expectations_met', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('planning_and_organization', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('risk_management', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('flexibility', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('post_implementation_support', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('training_and_documentation', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('business_impact', models.TextField(blank=True, null=True)),
                ('efficiency_improvement', models.TextField(blank=True, null=True)),
                ('user_adoption', models.TextField(blank=True, null=True)),
                ('areas_for_improvement', models.TextField(blank=True, null=True)),
                ('additional_comments', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
                ('submitted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'project_feedback',
            },
        ),
    ]
