from django.db import models
from opportunity.models import Opportunity
# Create your models here.
from django.core.validators import MinValueValidator,MaxValueValidator
from users.models import CustomUser
from django.core.exceptions import ValidationError

class Project(models.Model):

    class GateStatus(models.TextChoices):
        IDEATION = 'Ideation', 'Ideation'
        SCOPE = 'Scope', 'Scope'
        PLANNING = 'Planning', 'Planning'
        DEVELOPMENT = 'Development', 'Development'
        REALISATION = 'Realisation', 'Realisation'
        REVIEW = 'Review', 'Review'
        CLOSURE = 'Closure', 'Closure'
    
    class ProjectStatus(models.TextChoices):
        ACTIVE = 'Active', 'Active'
        COMPLETED = 'Completed', 'Completed'
        CANCELLED = 'Cancelled', 'Cancelled'
    
    class RagStatus(models.TextChoices):
        R = 'R', 'Red'
        A= 'A','Amber'
        G = 'G', 'Green'
    
    class ProjectType(models.TextChoices):
        Data = 'Data', 'Data'
        Application= 'Application','Application'
        ApplicationAndData= 'Application and Data','Application and Data'
        StrategicFacilityProjects= 'Strategic Facility Projects','Strategic Facility Projects'
        RegionalProjects= 'Regional Projects','Regional Projects'
    
    class DivisionStatus(models.TextChoices):
        VSS = 'VSS', 'VSS'
        VSC = 'VSC', 'VSC'

    name=models.CharField(max_length=150,null=True, blank=True)
    opportunity=models.ForeignKey(Opportunity,on_delete=models.SET_NULL,null=True)
    description=models.TextField(null=True, blank=True)
    objective=models.TextField(null=True, blank=True)
    type=models.CharField(max_length=50,null=True, blank=True,choices=ProjectType.choices)    
    product_owner=models.CharField(max_length=150,null=True, blank=True)
    lead_developer=models.CharField(max_length=150,null=True, blank=True)
    project_sponsor=models.CharField(max_length=150,null=True, blank=True)
    project_manager=models.CharField(max_length=150,null=True, blank=True)
    general_manager=models.JSONField(null=True, blank=True)
    development_sponsor=models.CharField(max_length=150,null=True, blank=True)
    gate=models.CharField(
        max_length=20,
        choices=GateStatus.choices,
        default=GateStatus.IDEATION
    )
    baseline_delivery_date=models.CharField(max_length=100,null=True, blank=True)
    actual_delivery_date=models.CharField(max_length=100,null=True, blank=True)
    status=models.CharField(
        max_length=10,
        choices=ProjectStatus.choices,
        default=ProjectStatus.ACTIVE
    )
    scope=models.CharField(
        max_length=10,
        choices=RagStatus.choices,
        default=RagStatus.G
    )
    cost=models.CharField(
        max_length=10,
        choices=RagStatus.choices,
        default=RagStatus.G

    )
    quality=models.CharField(
        max_length=10,
        choices=RagStatus.choices,
        default=RagStatus.G

    )
    time=models.CharField(
        max_length=10,
        choices=RagStatus.choices,
        default=RagStatus.G
    )
    division_type=models.CharField(
        max_length=10,
        choices=DivisionStatus.choices,
        default=DivisionStatus.VSS
    )
    team_member=models.ManyToManyField(CustomUser,related_name='projects',blank=True)
    created_by=models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True)
    start_date = models.DateField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        ordering = ['-created_at']
        db_table = 'project'
    

    def __str__(self):
        return self.name
    


class Costs(models.Model):
    id=models.CharField(max_length=10,primary_key=True,editable=False)
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    category = models.CharField(max_length=150, null=True, blank=True)
    group = models.CharField(max_length=150, null=True, blank=True)
    budget = models.CharField(max_length=150, null=True, blank=True)
    spent = models.CharField(max_length=150, null=True, blank=True)
    remaining_budget = models.CharField(max_length=150, null=True, blank=True)
    spend_to_finish = models.CharField(max_length=150, null=True, blank=True)
    forecast = models.CharField(max_length=150, null=True, blank=True)
    variance = models.CharField(max_length=150, null=True, blank=True)
    description=models.TextField(null=True,blank=True)
    additional_comment=models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
            db_table='project_cost'

    def save(self,*args,**kwargs):
        if not self.id:
            last_record=Costs.objects.all().order_by('id').last()
            if not last_record:
                new_id='C01'
            else:
                last_id=last_record.id
                new_id='C' + str(int(last_id[1:]) + 1).zfill(2)
            self.id=new_id
        
        # Calculate forecast
        try:
            spent_value = float(self.spent) if self.spent else 0.0
            spend_to_finish_value = float(self.spend_to_finish) if self.spend_to_finish else 0.0
            self.forecast = str(spent_value + spend_to_finish_value)
        except ValueError:
            raise ValidationError("Spent and Spend to Finish must be valid numbers.")

        # Calculate variance
        try:
            budget_value = float(self.budget) if self.budget else 0.0
            forecast_value = float(self.forecast)
            self.variance = str(budget_value - forecast_value)
        except ValueError:
            raise ValidationError("Budget and Forecast must be valid numbers.")

        super().save(*args, **kwargs)
        


    


class Risk(models.Model):
    class RiskChoices(models.TextChoices):
        ASSEMBLY_MANUFACTURING = 'assembly_manufacturing', 'Assembly Manufacturing'
        COMMUNICATION = 'communication', 'Communication'
        FACILITY_READINESS = 'facility_readiness', 'Facility Readiness'
        CUSTOMER = 'customer', 'Customer'
        FINANCE = 'finance', 'Finance'
        IT = 'it', 'IT'
        LOGISTICS = 'logistics', 'Logistics'
        MACHINERY_MANUFACTURING = 'machinery_manufacturing', 'Machinery Manufacturing'
        MARKETING = 'marketing', 'Marketing'
        PEOPLE = 'people', 'People'
        PLANNING = 'planning', 'Planning'
        PROCUREMENT = 'procurement', 'Procurement'
        QUALITY = 'quality', 'Quality'
        SAFETY = 'safety', 'Safety'
    
    id=models.CharField(max_length=10,primary_key=True,editable=False)
    name = models.CharField(max_length=150, null=True, blank=True)
    category = models.CharField(max_length=100,choices=RiskChoices.choices,null=True, blank=True)
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    probability = models.CharField(max_length=150, null=True, blank=True)
    impact = models.CharField(max_length=150, null=True, blank=True)
    risk_level = models.CharField(max_length=150, null=True, blank=True)
    risk_owner = models.CharField(max_length=150, null=True, blank=True)
    source = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(null=True,blank=True)
    risk_response = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    def calculate_risk_level(self):
        try:
            probability = int(self.probability) if self.probability is not None else 0
            impact = int(self.impact) if self.impact is not None else 0
            return probability * impact
        except ValueError:
            return 0

    def generate_risk_id(self):
        if self.category:
            # Split by underscore and then by spaces
            parts = self.category.lower().split('_')
            
            if len(parts) == 1:
                # Single part case (no underscores)
                prefix = parts[0][:2].upper()  # Take the first two letters of the single part
            else:
                # Multi-part case (with underscores)
                prefix = ''.join(part[0].upper() for part in parts[:2])  # Take first letter of each part up to the first two parts
            
            # Fetch the last record with the same prefix
            last_record = Risk.objects.filter(id__startswith=prefix).order_by('id').last()
            
            if not last_record:
                new_id = f'{prefix}01'
            else:
                last_id = last_record.id
                new_number = int(last_id[2:]) + 1
                new_id = f'{prefix}{str(new_number).zfill(2)}'
            
            return new_id
        
        return None


    def save(self, *args, **kwargs):
        if not self.id:
            self.id = self.generate_risk_id()
        self.risk_level = self.calculate_risk_level()
        super().save(*args, **kwargs)

    class Meta:
        db_table='project_risk'
    



class DecisionLog(models.Model):
   
    class ImpactChoices(models.TextChoices):
        Low = 'low', 'Low'
        Medium= 'medium','Medium'
        High= 'high', 'High'

    class StatusChoices(models.TextChoices):
        Pending = 'pending', 'Pending'
        Implemented= 'implemented','Implemented'

    id=models.CharField(max_length=10,primary_key=True,editable=False)
    impact = models.CharField(max_length=20, choices=ImpactChoices, default=ImpactChoices.Low)
    status = models.CharField(max_length=50,choices=StatusChoices, default=StatusChoices.Pending)
    detail = models.TextField(null=True,blank=True)
    resulting_action = models.TextField(null=True,blank=True)
    proposed_date = models.DateField(null=True,blank=True)
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    proposed_by = models.CharField(max_length=150,null=True,blank=True)
    approved_by = models.CharField(max_length=150,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    class Meta:
        db_table='project_decision_log'
    
    def save(self,*args,**kwargs):
        if not self.id:
            last_record=DecisionLog.objects.all().order_by('id').last()
            if not last_record:
                new_id='D01'
            else:
                last_id=last_record.id
                new_id='D' + str(int(last_id[1:]) + 1).zfill(2)
            self.id=new_id
        super().save(*args,**kwargs)


class ProjectFeedback(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    clarity_of_communication = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    responsiveness = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    collaboration = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    deliverable_quality = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    attention_to_detail = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    testing_and_validation = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    adherence_to_deadlines = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    time_management = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    knowledge_and_skills = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    problem_solving = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    overall_satisfaction = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    expectations_met = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    planning_and_organization = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    risk_management = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    flexibility = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    post_implementation_support = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    training_and_documentation = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    submitted_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    business_impact =  models.TextField(null=True,blank=True)
    efficiency_improvement =  models.TextField(null=True,blank=True)
    user_adoption =  models.TextField(null=True,blank=True)
    areas_for_improvement = models.TextField(null=True,blank=True)
    additional_comments = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table='project_feedback'